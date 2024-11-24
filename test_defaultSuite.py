# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestDefaultSuite():
  def setup_method(self, method):
    # self.driver = webdriver.Chrome()
    self.driver = webdriver.Firefox()
    self.driver.get("https://www.google.com/")
    self.driver.set_window_size(1536, 864)
    # self.driver.maximize_window()
    # self.driver.set_window_size(375, 667) # Iphone SE

  
  def teardown_method(self, method):
    self.driver.quit()
  
  def calculate_numbers(self,num1, num2):
    search_input = self.driver.find_element(By.NAME, "q")
    search_input.click()
    search_input.send_keys(f"{num1} + {num2}")
    
    # search_btn = self.driver.find_element(By.CSS_SELECTOR, "form > div:nth-child(1)")
    # search_btn.click()
    self.driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
    time.sleep(2)
  
  def test_testgoogle_sum_4plus7(self):
    self.calculate_numbers(4,7)

    try:
      search_result = self.driver.find_element(By.ID, "cwos")
      # element = self.driver.find_element(By.ID, "cwos")
      # actions = ActionChains(self.driver)
      # actions.move_to_element(element).perform()
    except selenium.common.exceptions.NoSuchElementException:
      self.driver.save_full_page_screenshot("google_error_sum_5plus6.png")

    assert search_result.text == "11"


  def test_testgoogle_sum_0plus17(self):
    self.calculate_numbers(0,17)
    
    try:
      search_result = self.driver.find_element(By.ID, "cwos")
      # element = self.driver.find_element(By.ID, "cwos")
      # actions = ActionChains(self.driver)
      # actions.move_to_element(element).perform()
    except selenium.common.exceptions.NoSuchElementException:
      self.driver.save_full_page_screenshot("google_error_sum_0plus17.png")

    assert search_result.text == "17"
  
   
