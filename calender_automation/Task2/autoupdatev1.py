from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from excel_handler import read_excel_links
import os

def debug_message(message):
    print(f"DEBUG: {message}")

options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
# options.add_argument("--headless")

service = Service()
driver = webdriver.Chrome(service=service, options=options)

def get_distance_between_elements(driver, element1, element2):
    location1 = element1.location
    location2 = element2.location
    return abs(location2['y'] - location1['y'])

def highlight_element(driver, element):
    driver.execute_script("arguments[0].style.border='3px solid red'", element)

def pixels_to_mm(pixels, dpi=96):
    return (pixels / dpi) * 25.4

try:
    
    print("Current Working Directory:", os.getcwd())

    # File path to the Excel sheet
    excel_file = "sheet2.xlsx"
    column_name = "rtpLink"

    # Read links from the Excel file
    links = read_excel_links(excel_file, column_name)

    if not links:
        debug_message("No links found. Exiting the script.")
    else:
        for url in links:
            debug_message(f"Opening the URL: {url}")
            driver.get(url)
            
            # Process each page as required (example for months 2-24):
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

                    if distance_mm >= 13: 
                        print(f"Bleed measure correct for Month {month}")
                    else:
                        print(f"Bleed measure incorrect for Month {month}")

                except Exception as e:
                    debug_message(f"An error occurred for Month {month}: {e}")

            debug_message("Saving screenshot of the highlighted elements")
            driver.save_screenshot(f"screenshot_{url.split('=')[-1]}.png")

except Exception as e:
    debug_message(f"An error occurred: {e}")

finally:
    debug_message("Closing the browser")
    driver.quit()
