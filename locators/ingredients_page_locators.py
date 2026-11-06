from selenium.webdriver.common.by import By


class IngredientsPageLocators():
   
   INGREDIENTS_LIST = (By.CLASS_NAME, "BurgerIngredient_ingredient__1TVf6")
   POPUP_WINDOW = (By.XPATH, "//*[text()='Детали ингредиента']")
   BUTTON_X = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified__3V5XS')]")
   INGREDIENT_COUNTER = (By.CLASS_NAME, "counter_counter__num__3nue1")
   ADD_ZONA = (By.CSS_SELECTOR, ".BurgerConstructor_basket__list__l9dp_")