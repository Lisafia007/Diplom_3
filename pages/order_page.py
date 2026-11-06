import allure
import requests
import time
from locators import OrderPageLocators
from pages.base_page import BasePageBurgers
from data import URLS, ENDPOINTS


class OrderPage(BasePageBurgers):

   # Метод проверки значения счетчика "за всё время" 
   @allure.step("Проверяем значение счётчика «за всё время»")
   def check_count_all_time(self):
      count = self.wait_element_visibility(OrderPageLocators.ALL_TIME_COUNT).text
      return int(''.join(filter(str.isdigit, count)))

   # Метод проверки значения счетчика "за сегодня" 
   @allure.step("Проверяем значение счётчика «за сегодня»")
   def check_count_today(self): 
      count = self.wait_element_visibility(OrderPageLocators.TODAY_COUNT).text
      return int(''.join(filter(str.isdigit, count)))

   # Метод создания заказа через API POST-запрос
   @allure.step("Отправляем API POST-запрос на создание заказа")
   def create_order(self, headers, get_payload):
      response = requests.post(f'{URLS.BASE_URL}{ENDPOINTS.ENDPOINT_CREATE_ORDER}', data=get_payload, headers = headers)
      time.sleep(2)
      return response.json()['order']['number']

   # Метод получения номера заказа и отображение его в разделе В работе
   @allure.step("Получаем список всех номеров заказов в разделе «В работе»")
   def get_orders_in_progress(self):
      return self.wait_element_visibility(OrderPageLocators.ORDERS_IN_PROGRESS_SECTION).text
  