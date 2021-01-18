from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By
import time
import sys

url = 'https://www.delta.com'


# default search query
start_airport = "MCO"
destination_airport = "AGS"

if (len(sys.argv) >= 2):
  search_query = sys.argv[1]
  print(search_query)


with webdriver.Firefox() as driver:
    # Set timeout time 
    wait = WebDriverWait(driver, 10)
    driver.delete_all_cookies()

    # retrive url in headless browser
    driver.get(url)
    wait.until(presence_of_element_located((By.PARTIAL_LINK_TEXT, "Departure")))
    
    # find search box
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Departure').click()
    
    search = driver.find_element_by_id("search_input")
    search.send_keys(start_airport + Keys.RETURN)
    
    driver.find_element_by_class_name("search-flyout-close").click()

    driver.find_element_by_class_name("to-container").click()

    search = driver.find_element_by_id("search_input")
    search.send_keys(destination_airport + Keys.RETURN)

    driver.find_element_by_class_name("search-flyout-close").click()


    driver.find_element_by_class_name("trip-type-container").click()
    driver.find_element_by_id("ui-list-selectTripType0").click()

    driver.find_element_by_class_name("calenderDepartSpan").click()

    driver.find_element_by_xpath("//a[@aria-label='23 January 2021, Saturday']").click()
    driver.find_element_by_xpath("//a[@aria-label='27 February 2021, Saturday']").click()

    driver.find_element_by_class_name("donebutton").click()

    
    driver.find_element_by_xpath("//span[@aria-owns='passengers-desc']").click()

    driver.find_elements_by_id('ui-list-passengers0')

    driver.find_element_by_id('btn-book-submit').click()

    wait.until(presence_of_element_located((By.CLASS_NAME, "farecelloffered")))

    elements = driver.find_elements_by_xpath("//span[text()='Main Cabin Class']/parent::store")

    for element in elements:
      print(element)

   