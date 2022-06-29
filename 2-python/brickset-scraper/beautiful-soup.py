import requests
from bs4 import BeautifulSoup
import csv

# Cria o CSV para escrever os dados e o cabeçalho
f = csv.writer(open('z-artist-names.csv', 'w'))
f.writerow(['Name', 'Link'])

# Cria lista vazia para colocar as URLs
pages = []

# Cria lista de URLs passando hardcoded 4 posições
for i in range(1, 5):
    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ' + str(i) + '.htm'
    pages.append(url)

# Print para conferir a lista antes da iteração
print(pages)

# Iteração dentro das urls para requisitar os dados
for item in pages:

    # Pega a página e cria um objeto BeautifulSoup a partir dela
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')

    # Acha a classe AlphaNav no HTML e a remove
    last_links = soup.find(class_='AlphaNav')
    last_links.decompose()

    # Pega o texto da Div BodyText
    artist_name_list = soup.find(class_='BodyText')

    # Pega o texto de todas as tags <a> dentro do BodyText 'artist_name_list'
    artist_name_list_items = artist_name_list.find_all('a')

    # Create for loop to print out all artists' names
    #for artist_name in artist_name_list_items:
    #    print(artist_name.prettify())

    # Percorre as tags <a> pegando os dados necessários e escreve no CSV
    for artist_name in artist_name_list_items:
        names = artist_name.contents[0]
        links = 'https://web.archive.org' + artist_name.get('href')
        # Add each artist’s name and associated link to a row
        f.writerow([names, links])