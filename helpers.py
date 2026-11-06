import random
import string
import requests
from data import URLS, ENDPOINTS



# Генерации случайных строк для создания уникального пользователя
def generate_random_user_data():
   random_string = "".join(random.choices(string.ascii_letters, k=8))
   return {
      "email": f"{random_string}@yandex.ru",
      "password": random_string,
      "name": random_string
   }

# Получение ингредиентов
def get_ingredients():
   ingredients = requests.get(f'{URLS.BASE_URL}{ENDPOINTS.ENDPOINT_GET_INGREDIENTS}')
   return ingredients.json()

# Формирование payload для создания заказа по индексу ингредиента
def make_order_payload(index=4):
   ingredients_data = get_ingredients()
   ing_id = ingredients_data['data'][index]['_id']
   return {"ingredients": [ing_id]}

