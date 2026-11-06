import allure
from pages import MainPageNavigation
from data import URLS



class TestMainPageNavigation:

   @allure.title("Проверка перехода по клику на Конструктор")   
   @allure.description("Нажимаем на Конструктор и переходим на главную страницу 'StellarBurgers'")
   def test_click_constructor_navigates_to_main(self, driver):    
      constructor = MainPageNavigation(driver)
      constructor.driver.get(URLS.BASE_URL)
      constructor.go_to_constructor()
 
      assert URLS.BASE_URL in constructor.get_current_url()


   @allure.title("Проверка перехода по клику на раздел Лента заказов")   
   @allure.description("Нажимаем на Лента заказов и переходим на страницу со списком заказов")
   def test_click_order_feed_navigates_to_feed(self, driver):
      order_feed = MainPageNavigation(driver)
      order_feed.driver.get(URLS.BASE_URL)
      order_feed.go_to_order_feed()

      assert URLS.ORDER_FEED_URL in order_feed.get_current_url()

