import pytest
import requests
from selenium import webdriver
from data import URLS, ENDPOINTS
from helpers import generate_random_user_data, make_order_payload


#Фикстура Драйвера
@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
   if request.param == "chrome":
      driver = webdriver.Chrome()
   elif request.param == "firefox":
      driver = webdriver.Firefox()

   request.addfinalizer(driver.quit)
   return driver

# Фукстура авторизации пользователя для получения токена
@pytest.fixture
def get_token():  

   payload = generate_random_user_data()

   requests.post(f'{URLS.BASE_URL}{ENDPOINTS.ENDPOINT_CREATE_USER}', data=payload)
   response = requests.post(f'{URLS.BASE_URL}{ENDPOINTS.ENDPOINT_USER_AUTHORIZATION}', data=payload)

   token = response.json().get("accessToken")
   headers = {"Authorization": token}

   yield headers
   # Удаление пользователя после теста
   requests.delete(f'{URLS.BASE_URL}{ENDPOINTS.ENDPOINT_USER_DELETION}', headers=headers)


# Фикстура для получения payload для тела запроса создания заказа
@pytest.fixture
def get_payload():
   return make_order_payload(index=4)
   