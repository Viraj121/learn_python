from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import time
from excel_handler import read_excel_links, store_incorrect_bleeds

def debug_message(message):
    print(f"DEBUG: {message}")

def get_distance_between_elements(driver, element1, element2):
    location1 = element1.location
    location2 = element2.location
    return abs(location2['y'] - location1['y'])

def highlight_element(driver, element):
    driver.execute_script("arguments[0].style.border='3px solid red'", element)

def pixels_to_mm(pixels, dpi=96):
    return (pixels / dpi) * 25.4

# Selenium setup
options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("--headless")

service = Service()
driver = webdriver.Chrome(service=service, options=options)

try:
    print("Current Working Directory:", os.getcwd())

    excel_file = "sheet2.xlsx"
    column_name = "rtpLink"

    incorrect_rtp_folder = "wrong_rtp"
    incorrect_rtp_file = "incorrect_bleeds.xlsx"

    links = read_excel_links("sheet2.xlsx", "rtpLink")

    if not links:
        debug_message("No links found. Exiting the script.")
    else:
        incorrect_bleeds = []  
        for url in links:
            debug_message(f"Opening the URL: {url}")
            driver.get(url)

            for month in range(2, 25, 2):
                month_name = f"//*[@id='hub_{month}']/div[1]/div/div[1]/div[1]"
                parent_div = f"//*[@id='hub_{month}']/div[1]/div" 
                try:
                    parent_div = driver.find_element(By.XPATH, parent_div)
                    month_name = driver.find_element(By.XPATH, month_name)
                    debug_message(f"Month : {month}")

                    driver.execute_script("arguments[0].scrollIntoView();", month_name)

                    driver.execute_script("""arguments[0].style.padding = '0px';
                                            arguments[0].style.margin = '0px';
                                            arguments[0].style.lineHeight = '1';  
                                            arguments[0].style.position = 'relative';""", month_name)

                    highlight_element(driver, month_name)
                    highlight_element(driver, parent_div)

                    distance = get_distance_between_elements(driver, month_name, parent_div)
                    distance_mm = pixels_to_mm(distance)

                    print(f"Distance for Month {month} in millimeters: {distance_mm:.2f} mm")

                    if distance_mm > 14: 
                        print(f"Bleed measure correct for Month {month}")
                    else:
                        print(f"Bleed measure incorrect for Month {month}")
                        incorrect_bleeds.append({
                            "Month": month,
                            "RTP Link": url,
                            "Distance (mm)": round(distance_mm, 2)
                        })
                        break
                    

                except Exception as e:
                    debug_message(f"An error occurred for Month {month}: {e}")

        if incorrect_bleeds:
            store_incorrect_bleeds(incorrect_rtp_folder, incorrect_rtp_file, incorrect_bleeds)

except Exception as e:
    debug_message(f"An error occurred: {e}")

finally:
    debug_message("Closing the browser")
    driver.quit()
