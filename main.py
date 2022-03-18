import threading, requests, json
from bs4 import BeautifulSoup

def main():
    array = ('filetype%3Apdf+test', 'enthec')
    pathfile = 'results.json'
    for search_item in array:
        t = threading.Thread(target=_scrapper(search_item, pathfile))
        t.start()

def _json_writer(result_list: list, pathfile: str):
    '''
    Escribe los resultados en el archivo JSON
    '''

    for item in result_list:
        document = {
            'title':item[0],
            'url':item[1]
        }

        with open(pathfile) as reader:
            data = json.load(reader)
            data.append(document)
        with open(pathfile, 'w') as writer:
             json.dump(data, writer, indent=4)

# def _paginator(term: str, pathfile: str):
    '''
    He intentado crear el paginador, pero a veces me varia el numero de resultados
    que me devuelve, así que no acabo de saber como puedo hacerlo
    Si el numero fuera constante, seria tan secillo como
    añadir un &[numero resultados +1] al url para acceder a la siguiente pagina
    '''

#     result_list = []
#     user_agent = {
#         'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0'
#     }
#     bing_url = f"https://www.bing.com/search?q={term}"
#     response = requests.get(bing_url, headers=user_agent)
#     response.status_code
#     soup = BeautifulSoup(response.text, 'html.parser')
#     select_num_results = soup.select("li.b_algo > h2 > a")
#     print(len(select_num_results))
#     for result in select_num_results:
#         print(result.get_text())

def _scrapper(term: str, pathfile: str):

    '''
    Bing scrapper, obtiene los resultados y los muestra por pantalla (Titulo y URL)
    '''

    user_agent = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0'
    }
    bing_url = f"https://www.bing.com/search?q={term}"
    result_list_page = []

    response = requests.get(bing_url, headers=user_agent)
    response.raise_for_status()

    page_soup = BeautifulSoup(response.text, 'html.parser')
    result_block = page_soup.select("li.b_algo > h2 > a")

    print(f"{term}:")
    for result in result_block:
        result_list_page.append([result.get_text(), result.get_attribute_list("href")])

    print(result_list_page)
    _json_writer(result_list_page, pathfile)

if __name__ == '__main__':
    main()