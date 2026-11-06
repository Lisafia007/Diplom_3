import allure
from pages import OrderPage
from data import URLS



class TestOrder:

   @allure.title("Проверка увеличения числа счётчика «за всё время» при создании нового заказа")   
   @allure.description("Создаём заказ и проверяем увеличение числа счётчика «за всё время»")
   def test_create_order_increases_total_counter(self, driver, get_token, get_payload):
      total_counter = OrderPage(driver)
      total_counter.driver.get(URLS.ORDER_FEED_URL)

      initial_count = total_counter.check_count_all_time()
      
      total_counter.create_order(get_token, get_payload)
      total_counter.refresh()

      final_count = total_counter.check_count_all_time()
      assert final_count > initial_count


   @allure.title("Проверка увеличения числа счётчика «за сегодня» при создании нового заказа")   
   @allure.step("Создаём заказ и проверяем увеличение числа счётчика «за сегодня»")
   def test_create_order_increases_today_counter(self, driver, get_token, get_payload):
      total_counter = OrderPage(driver)
      total_counter.driver.get(URLS.ORDER_FEED_URL)

      initial_count = total_counter.check_count_today()
      
      total_counter.create_order(get_token, get_payload)
      total_counter.refresh()

      final_count = total_counter.check_count_today()
      assert final_count > initial_count 


   @allure.title("Проверка появления номера заказа в разделе «В работе» после его создания")   
   @allure.step("Создаём заказ и проверяем отображение его номера в разделе «В работе»")
   def test_new_order_appears_in_progress_section(self, driver, get_token, get_payload): 
      num_order = OrderPage(driver)
      num_order.driver.get(URLS.ORDER_FEED_URL)

      create_order_num = num_order.create_order(get_token, get_payload)
      num_order.refresh()
      numbers_orders = num_order.get_orders_in_progress()
      
      assert str(create_order_num) in numbers_orders
       

