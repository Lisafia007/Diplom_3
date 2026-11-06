import allure
from pages import IngredientsPage
from data import URLS


class TestIngredients:
    
   @allure.title("Проверка появления всплывающего окна при нажатии на ингредиент")   
   @allure.description("Нажимаем на ингредиент и ожидаем всплывающее окно с деталями")
   def test_click_ingredient_opens_popup_window(self, driver):

      ingredient_page = IngredientsPage(driver)
      ingredient_page.driver.get(URLS.BASE_URL)
      ingredient_page.click_ingrient() 

      assert ingredient_page.is_popup_window_displayed()

     
   @allure.title("Проверка закрытия всплывающего окна")   
   @allure.description("Закрываем всплывающего окна, нажиматием на крестик")
   def test_close_ingredient_modal(self, driver):
      
      close_modal = IngredientsPage(driver)
      close_modal.driver.get(URLS.BASE_URL)
      close_modal.opens_modal()
      close_modal.click_on_x()

      assert close_modal.check_close()


   @allure.title("Проверка увеличение счетчика ингредиента при добовлении его в заказ")   
   @allure.description("Добавляем ингредиент в заказ и следим за увеличением его счётчика")
   def test_add_ingredient_increases_counter(self, driver):
      count = IngredientsPage(driver)
      count.driver.get(URLS.BASE_URL)

      initial_count = count.check_count()
      count.add_ingredient_to_order()
      final_count = count.check_count()

      assert final_count == initial_count + 2

