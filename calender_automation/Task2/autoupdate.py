from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def debug_message(message):
    print(f"DEBUG: {message}")

options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
# options.add_argument("--start-fullscreen")
options.add_argument("--headless")

service = Service()  
driver = webdriver.Chrome(service=service, options=options)

def get_distance_between_elements(driver, element1, element2):
    location1 = element1.location
    location2 = element2.location
    return abs(location2['y'] - (location1['y']))


def highlight_element(driver, element):
    """Highlights a Selenium WebElement by adding a red border."""
    driver.execute_script("arguments[0].style.border='3px solid red'", element)

def pixels_to_mm(pixels, dpi=96):
    """Converts pixels to millimeters (assuming 96 DPI)."""
    return (pixels / dpi) * 25.4

try:

    # url="https://rtp.pixika.ai/v2/pdf/index.php?tt=1735209761&product=DIYCALENDAR&source=cam&objectKey=67655b0757e577725&preview=stitch-done"
    url="https://rtp.pixika.ai/v2/pdf/index.php?tt=1734930378&product=DIYCALENDAR&source=cam&objectKey=6761887436e1df144&preview=stitch-done"
    # url="https://rtp.pixika.ai/v2/pdf/index.php?tt=1735028631&product=DIYCALENDAR&source=cam&objectKey=67638b482d93e1863&preview=stitch-done"
    # url="https://rtp.pixika.ai/v2/pdf/index.php?tt=1735028631&product=DIYCALENDAR&source=cam&objectKey=67652c1d2bc923b13&preview=stitch-done"
    # url = "https://rtp.pixika.ai/v2/pdf/index.php?tt=1733996851&product=DIYCALENDAR&source=cam&objectKey=67572defac8fe0fe5&preview=stitch-done%27"
    # url = "https://rtp.pixika.ai/v2/pdf/index.php?tt=1734966981&product=DIYCALENDAR&source=cam&objectKey=675d98737d8b8092b&preview=stitch-done"
    debug_message("Opening the URL")
    driver.get(url)
    # time.sleep(5) 

    debug_message("Page loaded successfully")

    for month in range(2,25,2):
        month_name = f"//*[@id='hub_{month}']/div[1]/div/div[1]/div[1]"
        parent_div = f"//*[@id='hub_{month}']/div[1]/div" 
        try:
            parent_div = driver.find_element(By.XPATH, parent_div)
            month_name = driver.find_element(By.XPATH, month_name)
            debug_message(f"Month : {month}")

            driver.execute_script("arguments[0].scrollIntoView();", month_name)
            # time.sleep(2)


            driver.execute_script("""arguments[0].style.padding = '0px';
                                    arguments[0].style.margin = '0px';
                                    arguments[0].style.lineHeight = '1';  
                                    arguments[0].style.position = 'relative';""", month_name)

            highlight_element(driver, month_name)
            highlight_element(driver, parent_div)
            time.sleep(4)

            distance = get_distance_between_elements(driver, month_name, parent_div)
           
            distance_mm = pixels_to_mm(distance)

            print(f"Distance for Month {month} in millimeters: {distance_mm:.2f} mm")

            
            if distance_mm >= 13: 
                print(f"Bleed measure correct for Month {month} ")
            else:
                print(f"Bleed measure incorrect for Month {month}")

        except Exception as e:
            debug_message(f"An error occurred for Month {month}: {e}")

   
    debug_message("Saving screenshot of the highlighted elements")
    driver.save_screenshot("screenshot.png")

except Exception as e:
    debug_message(f"An error occurred: {e}")

finally:
    debug_message("Closing the browser")
    driver.quit()
