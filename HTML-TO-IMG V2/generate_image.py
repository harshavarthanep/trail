import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

#Functionality
def html_to_image(html_file, output_dir):
    #Configure headless Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=400,400")  #Screen capture area default: "--window-size=1920,1080"

    #Initialize driver
    driver = webdriver.Chrome(options=chrome_options)

    #Open HTML file in Chrome
    driver.get(f"file://{html_file}")

    #Wait for page to load
    time.sleep(2)

    #Generate filename
    output_image = os.path.join(output_dir, f"WA{image_count:03d}.png") # "WA" is a sample text, image_count: "03d" here "03" is "001" number of digits

    #Take screenshot of the webpage
    driver.save_screenshot(output_image)

    #Quit Chrome driver
    driver.quit()

    return output_image

#Path to the HTML file
html_file = "/D:/2023/CAREER/CREATINK/Web%20Development/PROJECTS/HTML%20TO%20IMG%20V2/template.html"

#Output directory for the image files
output_dir = "Outputs"

#Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

#Count of images generated
image_count = len(os.listdir(output_dir)) + 1

#Convert HTML to image
output_image = html_to_image(html_file, output_dir)

#Confirm Image Download
print(f"HTML file converted to image: {output_image}")
