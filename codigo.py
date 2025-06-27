import requests
from bs4 import BeautifulSoup as bs

def extrairLivros():

    url = requests.get('https://books.toscrape.com/')
    dadosDoSite = bs(url.text, 'html.parser')
    livros = dadosDoSite.find_all('article', class_="product_pod")

    for livro in livros:
        nomeLivro = livro.h3.a['title']
        custo = livro.find('p', class_="price_color").text
        print(f"Nome do Livro: {nomeLivro} \nCusto: {custo} \n")
        print("-=-" * 20) # Linha improvisada para separar os livros apenas

extrairLivros()