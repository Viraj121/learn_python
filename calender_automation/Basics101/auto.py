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
options.add_argument("--headless")  # Run in headless mode for debugging purposes if required
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

# Use WebDriver Manager to handle ChromeDriver installation
def get_webdriver():
    from webdriver_manager.chrome import ChromeDriverManager
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver = get_webdriver()

try:
    # Open the specified URL
    url = "https://rtp.pixika.ai/v2/pdf/index.php?tt=1733996851&product=DIYCALENDAR&source=cam&objectKey=67572defac8fe0fe5&preview=stitch-done%27"
    debug_message("Opening the URL")
    driver.get(url)
    time.sleep(5)  # Allow the page to load

    debug_message("Page loaded successfully")

    # Initialize variables
    planner_months = []
    
    # Loop to extract month names (XPath assumes the pattern is consistent)
    for i in range(2, 27, 2):  # Step of 2 to skip calendar elements
        xpath = f"//*[@id=\"hub_{i}\"]/div[1]/div/div[1]/div[1]"
        try:
            # Locate the month name element
            element = driver.find_element(By.XPATH, xpath)
            month_name = element.text
            planner_months.append(month_name)
            debug_message(f"Extracted month name: {month_name}")
        except Exception as e:
            debug_message(f"Error extracting month for XPath hub_{i}: {e}")

    # Print all extracted months
    debug_message("Extraction complete. Printing all planner months.")
    for month in planner_months:
        print(month)

except Exception as e:
    debug_message(f"An error occurred: {e}")

finally:
    # Close the browser
    debug_message("Closing the browser")
    driver.quit()
