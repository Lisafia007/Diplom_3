from selenium.webdriver.common.by import By


class OrderPageLocators:
   
   ALL_TIME_COUNT = (By.XPATH, "//*[contains(text(), 'Выполнено за все время')]/following-sibling::p")
   TODAY_COUNT = (By.XPATH, "//*[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")
   ORDERS_IN_PROGRESS_SECTION = (By.XPATH, "//*[contains(text(), 'В работе')]/following-sibling::*[contains(@class, 'OrderFeed_orderListReady')]")