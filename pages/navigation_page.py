import allure
from locators import NavigationPageLocators, BasePageLocators
from pages.base_page import BasePageBurgers
from data.urls import URLS


class MainPageNavigation(BasePageBurgers):

   #Метод перехода по клику на "Конструктор"
   @allure.step("Нажимаем на Коструктор")
   def go_to_constructor(self):
      self.wait_element_invisibility(BasePageLocators.MODAL_OVERLAY)
      self.wait_element_to_be_clickable(NavigationPageLocators.BUTTON_CONSTRUCTOR).click()
      self.wait_url_contains(URLS.BASE_URL)

   #Метод перехода по клику на "Лента заказа"
   @allure.step("Нажимаем на Лента заказа")
   def go_to_order_feed(self):
      self.wait_element_invisibility(BasePageLocators.MODAL_OVERLAY)
      self.wait_element_to_be_clickable(NavigationPageLocators.BUTTON_ORDER_FEED).click()
      self.wait_url_contains(URLS.ORDER_FEED_URL)