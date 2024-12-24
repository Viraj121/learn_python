from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
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

def pixels_to_mm(pixels, dpi=96):
    """Converts pixels to millimeters (assuming 96 DPI)."""
    return (pixels / dpi) * 25.4

try:
    # Open the specified URL
    url = "https://rtp.pixika.ai/v2/pdf/index.php?tt=1734966981&product=DIYCALENDAR&source=cam&objectKey=675d98737d8b8092b&preview=stitch-done"
    debug_message("Opening the URL")
    driver.get(url)
    time.sleep(5)  # Allow the page to load

    debug_message("Page loaded successfully")

    # Loop through each month (from January to December)
    for month in range(1, 13):  # Loop through months 1 to 12
        # Determine the XPath for the planner and calendar elements for each month
        # Adjust the XPath patterns dynamically based on the current month
        planner_xpath = f"//*[@id='hub_{month}']/div[1]/div/div[1]/div[1]"  # Example XPath for planner
        calendar_xpath = f"//*[@id='hub_{month}']/div[2]/div/div[1]/div[1]"  # Example XPath for calendar
        
        # Locate the planner and calendar elements
        try:
            planner_element = driver.find_element(By.XPATH, planner_xpath)
            calendar_element = driver.find_element(By.XPATH, calendar_xpath)

            # Debug message for current month
            debug_message(f"Located planner and calendar for Month {month}")

            # Scroll to the planner element to ensure it's visible
            debug_message(f"Scrolling to planner of Month {month}")
            driver.execute_script("arguments[0].scrollIntoView();", planner_element)
            time.sleep(2)

            # Highlight the planner and calendar elements
            debug_message(f"Highlighting planner and calendar for Month {month}")
            highlight_element(driver, planner_element)
            highlight_element(driver, calendar_element)

            # Calculate the distance between the planner and calendar
            debug_message(f"Calculating the space between planner and calendar for Month {month}")
            distance = get_distance_between_elements(driver, planner_element, calendar_element)
            debug_message(f"Calculated distance for Month {month}: {distance} pixels")

            # Convert the distance from pixels to millimeters
            distance_mm = pixels_to_mm(distance)
            debug_message(f"Converted distance for Month {month}: {distance_mm:.2f} mm")
            print(f"Distance for Month {month} in millimeters: {distance_mm:.2f} mm")

            # Check if the bleed measurement is correct (for each month)
            if distance_mm >= 13:  # Minimum 13 mm distance
                print(f"Bleed measure correct for Month {month}")
            else:
                print(f"Bleed measure incorrect for Month {month}")

        except Exception as e:
            debug_message(f"An error occurred for Month {month}: {e}")

    # Save the screenshot
    debug_message("Saving screenshot of the highlighted elements")
    driver.save_screenshot("highlighted_planners.png")

except Exception as e:
    debug_message(f"An error occurred: {e}")

finally:
    # Close the browser
    debug_message("Closing the browser")
    driver.quit()
