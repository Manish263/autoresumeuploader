from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Configuration
email = 'manishk26799@gmail.com'  # Update with your Naukri.com login email
password = 'Manish@8955'  # Update with your Naukri.com account password
resume_path = r"C:/Users/manis/OneDrive/Desktop/Resume-MANISH.pdf"  # Update with the correct path to your resume
naukri_profile_url = 'https://www.naukri.com/mnjuser/profile?id=&altresid'

def upload_resume():
    # Setup WebDriver
    driver_path = r"C:/Users/manis/OneDrive/Desktop/automate/chromedriver.exe"  # Update with the path to your ChromeDriver
    driver = webdriver.Chrome()

    try:
        # Open Naukri login page
        driver.get('https://www.naukri.com/nlogin/login')

        # Login
        email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'usernameField')))
        email_field.send_keys(email)

        password_field = driver.find_element(By.ID, 'passwordField')
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

        # Wait for login to complete
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#mainHeader')))
            print("Login successful.")
        except TimeoutException:
            print("Login timeout. Check if login was successful.")

        # Navigate to Profile page
        driver.get(naukri_profile_url)

        # Wait for profile page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="file"]')))

        # Upload resume
        upload_button = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
        upload_button.send_keys(resume_path)

        # Optionally, you can add a wait to ensure the upload completes
        time.sleep(10)  # Adjust based on your internet speed

        print("Resume uploaded successfully.")

    finally:
        driver.quit()

# Call the upload_resume function directly
upload_resume()
