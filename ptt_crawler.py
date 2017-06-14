import requests
import urllib.parse
from bs4 import BeautifulSoup


BOARD_URL_MAPPER = {
    'movie': 'movie'
}

def board_url(board_name):
    url = 'https://www.ptt.cc/bbs/{}/index.html'.format(BOARD_URL_MAPPER[board_name])
    return url


NOT_EXIST = BeautifulSoup('<a>本文已被刪除</a>', 'lxml').a


def get_posts_from_page(url):
    """get the list from the board
    """
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'lxml')
    articles = soup.find_all('div', 'r-ent')

    posts = []

    for article in articles:

        meta = article.find('div', 'title').find('a') or NOT_EXIST
        posts.append({
            'title': meta.getText().strip(),
            'link': meta.get('href'),
            'push': article.find('div', 'nrec').getText(),
            'date': article.find('div', 'date').getText(),
            'author': article.find('div', 'author').getText(),
        })

    next_link = soup.find('div', 'btn-group-paging').find_all('a', 'btn')[1].get('href')

    return posts, next_link


def get_content(url):
    pass


if __name__ == '__main__':
    """not enough time..
    """
    posts, next_linet = get_posts_from_page(board_url('movie'))

    print(posts)
