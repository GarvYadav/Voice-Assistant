from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from os import getcwd


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--headless=new")


chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--allow-running-insecure-content")
chrome_options.add_argument("--disable-software-rasterizer")
chrome_options.add_argument("--allow-file-access-from-files")


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

website = "https://allorizenproject1.netlify.app/"

driver.get(website)
rec_file = f"{getcwd()}\\input.txt"






def listen():
    try:
        start_button = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID,'startButton')))
        start_button.click()
        print("Listening...")
        output_text = ""
        is_second_click = False
        while True:
            output_element = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.ID,'output')))
            current_text = output_element.text.strip()
            if "Start Listening" in start_button.text and is_second_click:
                if output_text:
                    is_second_click = False
            elif "Listening..." in start_button.text:
                is_second_click = True
            if current_text!=output_text:
                output_text = current_text
                with open(rec_file, "w") as f:
                    f.write(output_text.lower())
                    print("USER:" + output_text)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
        
        
listen()