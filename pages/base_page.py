import allure
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePageBurgers():

   def __init__(self, driver):
      self.driver = driver

   def wait_element_visibility(self, loc_path, wait_time = 15):
      return WebDriverWait(self.driver, wait_time).until(expected_conditions.visibility_of_element_located(loc_path))

   def wait_element_to_be_clickable(self, loc_path, wait_time = 15):
      return WebDriverWait(self.driver, wait_time).until(expected_conditions.element_to_be_clickable(loc_path))

   def element(self, loc_path):
      first_element = self.driver.find_elements(*loc_path)
      return first_element[0]

   #Метод открытия страницы  
   @allure.step("Открываем url")
   def open(self, url):
      self.driver.get(url)

   #Метод для ожидания загрузки url 
   @allure.step("Ожидаем загрузку url страницы")
   def wait_url_contains(self, url_part, wait_time=15):
      WebDriverWait(self.driver, wait_time).until(
      expected_conditions.url_contains(url_part))

   #Метод проверки отображения элемента на странице 
   @allure.step("Проверяем, отображается ли элемент на странице")
   def is_element_displayed(self, loc_path):
      return self.element(loc_path).is_displayed()

   #Метод проверки текущей открытой страницы 
   @allure.step("Проверяем текущий url страницы")
   def get_current_url(self):
      return self.driver.current_url

   #Метод для ожидания исчезновения элемента с экрана
   @allure.step("Ожидаем исчезновения элемента с экрана")
   def wait_element_invisibility(self, loc_path, wait_time=15):
      return WebDriverWait(self.driver, wait_time).until(
         expected_conditions.invisibility_of_element_located(loc_path))

   #Метод перезагрузки страницы
   @allure.step("Перезагружаем данные страницы")
   def refresh(self):
      self.driver.refresh()
      time.sleep(2)