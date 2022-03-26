import requests
from bs4 import BeautifulSoup


class GetImages:

    def __init__(self):
        self.links = None
        self.req = None
        self.soup = None
        self.session = None
        self.hdr = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/99.0.4844.74 Safari/537.36 ',
            'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, * / *;q = 0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'
            }

    def create_request(self, url):
        self.session = requests.session()
        self.req = self.session.get(url, headers=self.hdr)
        self.soup = BeautifulSoup(self.req.content, 'lxml')

    def pull_images_url(self, dict_images):
        self.links = self.soup.find('body').findAll('a', {'class': '_LIsc'})

        for link in self.links:
            final_link = link.find('img')

            if final_link['src'] != '':
                dict_images.append(final_link['src'])

# https://unsplash.com/s/photos/
