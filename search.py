import requests
from bs4 import BeautifulSoup
import os

def create_dir(dir):
    try:
        os.makedir(dir)
    else:
        pass

def main():
    pages = int(input("Enter the number of pages: "))
    q = input("Enter your search query: ")
    create_dir(q)
    url = "https://yandex.ru/images/search?text={}".format(q)
    number = 0
    for p in range(pages):
        page = requests.get(url+"&p={}".format(p))
        soup = BeautifulSoup(page.text, "html.parser")
        pictures = soup.findAll(class_='serp-item__thumb justifier__thumb')
        for picture in pictures:
            picture = 'http:'+picture.get('src')
            picture = requests.get(picture)
            with open("./{}/{}.png".format(q, number), "wb") as code:
                code.write(picture.content)
            number+=1



if __name__ == "__main__":
    main()
