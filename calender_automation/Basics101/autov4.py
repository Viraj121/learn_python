from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import time

# Debug function
def debug_message(message):
    print(f"DEBUG: {message}")

# Set up the WebDriver (Chrome in this case)
options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

service = Service()  # Updated to avoid specifying the chromedriver path explicitly
driver = webdriver.Chrome(service=service, options=options)

def get_distance_between_elements(driver, element1, element2):
    location1 = element1.location
    location2 = element2.location
    return abs(location2['y'] - location1['y'])

def highlight_element(driver, element):
    """Highlights a Selenium WebElement by adding a red border."""
    driver.execute_script("arguments[0].style.border='2px solid red'", element)

try:
    # Open the specified URL

    # url = "https://rtp.pixika.ai/v2/pdf/index.php?tt=1733996851&product=DIYCALENDAR&source=cam&objectKey=67572defac8fe0fe5&preview=stitch-done%27"
    url="https://rtp.pixika.ai/v2/pdf/index.php?tt=1734966981&product=DIYCALENDAR&source=cam&objectKey=675d98737d8b8092b&preview=stitch-done"

    debug_message("Opening the URL")
    driver.get(url)
    time.sleep(5)  # Allow the page to load

    debug_message("Page loaded successfully")

    # Locate the FEB month name of the planner
    feb_month_xpath = "//*[@id=\"hub_2\"]/div[1]/div/div[1]/div[1]"
    feb_month_element = driver.find_element(By.XPATH, feb_month_xpath)
    debug_message("Located FEB month name element")

    # Scroll to the FEB planner
    debug_message("Scrolling to FEB planner")
    driver.execute_script("arguments[0].scrollIntoView();", feb_month_element)
    time.sleep(2)

    # Remove padding of FEB month element
    debug_message("Removing padding for FEB month name element")
    driver.execute_script("arguments[0].style.padding = '0px';", feb_month_element)

    # Highlight FEB month name element
    debug_message("Highlighting FEB month name element")
    highlight_element(driver, feb_month_element)

    # Locate the parent div of the planner
    parent_div_xpath = "//*[@id=\"hub_2\"]/div[1]/div"
    parent_div_element = driver.find_element(By.XPATH, parent_div_xpath)
    debug_message("Located parent div of the planner")
    time.sleep(5)

    # Highlight parent div of the planner
    debug_message("Highlighting parent div of the planner")
    highlight_element(driver, parent_div_element)
    time.sleep(6)

    # Calculate the space between FEB month name and its parent div
    debug_message("Calculating the space between FEB month name and its parent div")
    distance = get_distance_between_elements(driver, feb_month_element, parent_div_element)
    debug_message(f"Calculated distance: {distance} pixels")

# Convert the distance from pixels to millimeters (assuming 96 DPI)
    def pixels_to_mm(pixels, dpi=96):
        # 1 inch = 25.4 mm, and DPI = dots (pixels) per inch
        return (pixels / dpi) * 25.4

    distance_mm = pixels_to_mm(distance)
    debug_message(f"Converted distance: {distance_mm:.2f} mm")
    print(f"Distance in millimeters: {distance_mm:.2f} mm")

    # Check if the bleed measurement is correct
    if distance_mm >= 13:  # Minimum 13 mm distance
        print("Bleed measure correct")
    else:
        print("Bleed measure incorrect")


    # Save the screenshot
    debug_message("Saving screenshot of the highlighted elements")
    driver.save_screenshot("highlighted_feb_planner.png")

except Exception as e:
    debug_message(f"An error occurred: {e}")

finally:
    # Close the browser
    debug_message("Closing the browser")
    driver.quit()
