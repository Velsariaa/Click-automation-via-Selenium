from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import platform


if platform.system() == "Windows":
    chrome_binary_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
elif platform.system() == "Darwin": 
    chrome_binary_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
else:
    raise EnvironmentError("Unsupported operating system")

if not os.path.exists(chrome_binary_path):
    raise FileNotFoundError(f"Chrome executable not found at {chrome_binary_path}")

options = webdriver.ChromeOptions()
options.binary_location = chrome_binary_path

try:
    driver = webdriver.Chrome(options=options)
except Exception as e:
    print(f"Error initializing WebDriver: {e}")
    exit()

url = "https://animo.sys.dlsu.edu.ph/psp/ps/EMPLOYEE/HRMS/?cmd=logout"
driver.get(url)

time.sleep(3)

try:
    userid_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "userid"))
    )
    userid_field.send_keys("12326615")

    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "pwd"))
    )
    password_field.send_keys("Ilovebarn_2004!")

    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "Submit"))
    )
    submit_button.click()

    employee_service_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "fldra_CO_EMPLOYEE_SELF_SERVICE"))
    )
    employee_service_button.click()

    enrollment_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "fldra_HCCC_ENROLLMENT"))
    )
    enrollment_button.click()

    enrollment_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "crefli_HC_SSR_SSENRL_CART_GBL"))
    )
    enrollment_cart_button.click()
    
    iframe = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "ptifrmtgtframe"))
    )
    driver.switch_to.frame(iframe)
    
   
    max_iterations = 999999 
    current_iteration = 0

    while current_iteration < max_iterations:
        try:
            proceed_to_step_button = WebDriverWait(driver, 50).until(
                EC.element_to_be_clickable((By.ID, "DERIVED_REGFRM1_LINK_ADD_ENRL$114$"))
            )
            proceed_to_step_button.click()
            
            finish_enroll_button = WebDriverWait(driver, 50).until(
                EC.element_to_be_clickable((By.ID, "DERIVED_REGFRM1_SSR_PB_SUBMIT"))
            )
            finish_enroll_button.click()
            
            add_another_button = WebDriverWait(driver, 50).until(
                EC.element_to_be_clickable((By.ID, "DERIVED_REGFRM1_SSR_LINK_STARTOVER"))
            )
            add_another_button.click()
            
            current_iteration += 1
            print(f"Iteration {current_iteration} completed.")

            time.sleep(3)
        
        except Exception as e:
            print(f"Error during iteration {current_iteration}: {e}")
            break 

except Exception as e:
    print(f"Error during navigation process: {e}")

time.sleep(500000)