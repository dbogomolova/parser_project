import requests # Этот фрагмент кода импортирует библиотеку запросов в вашу программу на Python.
from bs4 import BeautifulSoup # эта строка подготавливает код к работе с библиотекой BeautifulSoup, позволяя легко перемещаться по веб-страницам и извлекать из них информацию.
def get_page_content(link):   #принимает ссылку и выводит ее содержимое
  response = requests.get(link) # эта строка кода похожа на отправку сообщения на веб-сайт с запросом его содержимого. Переменная response затем сохраняет ответ веб-сайта. 
  if response.status_code == 200:  # если статус = 200, то запрос успешен (на веб-сайте код состояния, равный 200, означает, что запрос успешно обработан сервером и запрошенный вами контент доступен)
      return response.content #  Эта строка кода извлекает данные с веб-сайта, которые запрашивали, и возвращает 'response'  в нашу программу

def parse_classics_page(link): # принимает ссылку и выводит ее содержимое
    response = requests.get(link) # эта строка кода отправляет веб-сайту сообщение с запросом о его содержимом. Затем веб-сайт отправляет ответ, который сохраняется в переменной response. 
    response.raise_for_status()  # Проверим наличие ошибок HTTP (это важно, для того, чтобы ваш код корректно обрабатывал запрос. Это помогает предотвратить неожиданный сбой в работе вашей программы и дает вам возможность соответствующим образом обработать ошибку.)
    soup = BeautifulSoup(response.content, 'html.parser') # Этот фрагмент кода берет исходное HTML-содержимое веб-страницы, которое было получено с помощью requests.get(ссылка), и преобразует его в структурированный объект, называемый объектом BeautifulSoup.
    titles = [] # создаем пустой список для названий книг
    prices = [] # создаем пустой список для цен книг
    for book in soup.find_all('article', class_='product_pod'): # Этот фрагмент кода используется для перебора списка элементов книги на веб-странице.
        title = book.find('h3').find('a')['title'] # эта строка кода предназначена для извлечения полного названия книги с веб-страницы. Для этого выполняется навигация по HTML-структуре элемента book, поиск названия в теге привязки и извлечение его атрибута 'title'.
        price = book.find('p', class_='price_color').text.strip() # Этот фрагмент кода отвечает за извлечение цены на книгу из HTML-структуры веб-страницы.
        titles.append(title) # эта строка кода берет извлеченное название книги и добавляет его в конец списка названий
        prices.append(price) # эта строка кода берет извлеченную цену и добавляет ее в конец списка цен
    return titles, prices # получаем готовый список 