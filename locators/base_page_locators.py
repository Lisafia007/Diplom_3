from selenium.webdriver.common.by import By


class BasePageLocators:
   MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")
