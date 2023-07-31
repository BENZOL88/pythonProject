from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time

# Данные для аутентификации
username = 'acarev'
password = 'xW1PsZ8An0Pf'

# URL для аутентификации и URL страницы для парсинга
login_url = 'https://centiman.avito.ru/service-dataset-collector-frontend/login'
data_url = 'https://centiman.avito.ru/service-dataset-collector-frontend/project/741'

# Указываем путь к ChromeDriver (замените на свой путь)
chrome_driver_path = 'D:/path/to/chromedriver.exe'

# Создаем сервис ChromeDriver
service = ChromeService(executable_path=chrome_driver_path)

# Создаем экземпляр веб-драйвера Chrome
driver = webdriver.Chrome(service=service)

driver.get(login_url)

username_input = driver.find_element(by='css selector', value='#app > main > div > div > div.username > label > input[type=text]')
password_input = driver.find_element(by='css selector', value='#app > main > div > div > div.password > label > input[type=password]')

# Вводим логин и пароль
username_input.send_keys(username)
password_input.send_keys(password)

time.sleep(3)
# Отправляем форму (нажатие клавиши Enter)
driver.find_element(by='css selector', value='#app > main > div > div > div.button_site > div').click()
time.sleep(3)
# Загружаем страницу с данными


# Ждем некоторое время для загрузки страницы (при необходимости)


driver.get(data_url)
time.sleep(5)

# Находим элемент, из которого хотим извлечь данные
data_element = driver.find_element(by='css selector', value='#app > footer > div')
data = data_element.text
print(data)

# Закрываем браузер
#driver.quit()
