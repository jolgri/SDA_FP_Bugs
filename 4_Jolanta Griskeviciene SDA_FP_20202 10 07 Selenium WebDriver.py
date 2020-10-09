# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestJAVAEx():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_jAVAEx(self):
    # Test name: JAVA_Ex
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://homeworks.tester.en.sdacademy.pro/")
    # 2 | setWindowSize | 1296x696 | 
    #self.driver.set_window_size(1296, 696)
    # 3 | click | css=.md-nav__item--nested:nth-child(8) > .md-nav__link | 
    self.driver.find_element(By.CSS_SELECTOR, ".md-nav__item--nested:nth-child(8) > .md-nav__link").click()
    # 4 | click | linkText=Exercise 1 | 
    # self.driver.find_element(By.LINK_TEXT,"Exercise 25").click()
    time.sleep(3)
    for e in range(1,26,1):
        text = f"Exercise {e}"
        element = self.driver.find_element(By.CSS_SELECTOR, ".md-sidebar--primary > .md-sidebar__scrollwrap")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".md-sidebar--primary > .md-sidebar__scrollwrap")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".md-sidebar--primary > .md-sidebar__scrollwrap")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.LINK_TEXT, text).click()
        self.driver.find_element(By.LINK_TEXT, "Solution").click()
        self.driver.find_element(By.LINK_TEXT, "code").click()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)     
      
if __name__ == "__main__":
  test = TestJAVAEx()
  test.setup_method("Bet kas")
  test.test_jAVAEx()
