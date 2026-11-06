import allure
from locators import IngredientsPageLocators, BasePageLocators
from pages.base_page import BasePageBurgers



class IngredientsPage(BasePageBurgers):

   # Метод нажатия на ингредиент 
   @allure.step("Нажимаем на ингредиент")
   def click_ingrient(self):
      self.wait_element_invisibility(BasePageLocators.MODAL_OVERLAY)
      self.wait_element_to_be_clickable(IngredientsPageLocators.INGREDIENTS_LIST)
      ingredient = self.element(IngredientsPageLocators.INGREDIENTS_LIST)
      self.driver.execute_script("arguments[0].click();", ingredient)

   # Проверка открытия окна с деталями ингредиента
   @allure.step("Проверяем, отображается ли окно с деталями ингредиента на странице")
   def is_popup_window_displayed(self):
      self.wait_element_visibility(IngredientsPageLocators.POPUP_WINDOW)
      return self.is_element_displayed(IngredientsPageLocators.POPUP_WINDOW)

   #Объединение методов для открытия окна с деталями ингредиента
   @allure.step("Объединяем методы для открытия окна с деталями ингредиента в шаг")
   def opens_modal(self):
      self.click_ingrient()
      self.is_popup_window_displayed()

   # Метод нажатия на крестик для закрытия окна с деталями ингредиента
   @allure.step("Закрываем окно с деталями ингретиента, нажатием на крестик")
   def click_on_x(self):
      button_x = self.wait_element_to_be_clickable(IngredientsPageLocators.BUTTON_X)
      self.driver.execute_script("arguments[0].click();", button_x)

   # Метод проверки закрытия окна с деталями ингредиента
   @allure.step("Проверяем закрытие окна с деталями ингретиента после нажатием на крестик")
   def check_close(self):
      return self.wait_element_invisibility(IngredientsPageLocators.POPUP_WINDOW)

   # Метод проверки значения счетчика ингредиента 
   @allure.step("Проверяем значение счетчика ингредиента")
   def check_count(self):
      self.wait_element_visibility(IngredientsPageLocators.INGREDIENT_COUNTER)
      count = self.element(IngredientsPageLocators.INGREDIENT_COUNTER)
      return int(count.text)

   # Метод добавления ингредиента в заказ
   @allure.step("Перетаскиваем ингредиент для добавления в заказ через JavaScriprt")
   def add_ingredient_to_order(self):
     
      ingredient = self.element(IngredientsPageLocators.INGREDIENTS_LIST)
      add_zona = self.wait_element_visibility(IngredientsPageLocators.ADD_ZONA)

      self.driver.execute_script("""
         var source = arguments[0];
         var target = arguments[1];

         var evt = document.createEvent("DragEvent");
         evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
         source.dispatchEvent(evt);

         evt = document.createEvent("DragEvent");
         evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
         target.dispatchEvent(evt);

         evt = document.createEvent("DragEvent");
         evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
         target.dispatchEvent(evt);

         evt = document.createEvent("DragEvent");
         evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
         target.dispatchEvent(evt);

         evt = document.createEvent("DragEvent");
         evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
         source.dispatchEvent(evt);
         """, ingredient, add_zona)