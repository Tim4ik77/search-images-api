import requests
from bs4 import BeautifulSoup
import os

def main():
    n = int(input("Введите кол-во страниц: "))
    q = input("Введите поисковый запрос: ")
    q1 = eval(q)
    for q in q1:
        url = "https://yandex.ru/images/search?text={}".format(q)
        try:
            os.mkdir(q)
        except:
            pass
        number = 0
        for n1 in range(n):
            page = requests.get(url+"&p={}".format(n1))
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