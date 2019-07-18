import requests
from bs4 import BeautifulSoup

class Gamestorrent:
    
    def __init__(self):
        self.base_url = 'https://pcgamestorrents.com/'
    
    def search(self, query):
        titles = []
        page = requests.get('{} {} {}'.format(self.base_url, '?s=', query))
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find_all(class_='uk-article-title')
        [ titles.append(result.text) for result in results ]
        return titles
    
    def get_magnet(self, game_name):
        print('{}{}.html'.format(self.base_url, game_name.replace(' ', '-')))
        page = requests.get('{}{}.html'.format(self.base_url, game_name.replace(' ', '-')))
        soup = BeautifulSoup(page.content, 'html.parser')
        
        for a in soup.find_all('a', href=True):
            if 'magnet' in a['href']:
                return a['href']
        return 'No magnet found in page'
        