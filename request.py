import requests
from bs4 import BeautifulSoup


def get_goroscope(sign):
    """Функция получает гороском с сайта и возвращает его."""

    url = f'https://randomus.ru/horoscope/{sign}/common/random'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        content_div = soup.find('div', class_='content mb-0')

        if content_div:
            paragraph = content_div.find('p')

            if paragraph:
                horoscope_text = paragraph.get_text(strip=True)
                return f"Гороскоп на сегодня:\n\n {horoscope_text}"
        else:
            return "Не удалось найти гороскоп на странице."
    else:
        print(f"Ошибка при запросе страницы: {response.status_code}")
