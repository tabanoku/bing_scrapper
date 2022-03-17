#import os, json
import threading, requests
from bs4 import BeautifulSoup

def main():
    array = ("filetype%3Apdf+test", "enthec")
#    pathfile = _file_creator()

    for search_item in array:
        t = threading.Thread(target=_scrapper(search_item))
#        t = threading.Thread(target=_scrapper(search_item, pathfile))
        t.start()

# def _file_creator():
#     #abspath =  '.' + os.path.abspath(os.getcwd())
#     file_name = 'results.json'

#     if os.path.isfile(file_name):
        
#         expand = 1
        
#         while True:
#             expand += 1
#             new_file_name = file_name.split('.json')[0] + str(expand) + '.json'
           
#             if os.path.isfile(new_file_name):
#                 continue
#             else:
#                 file_name = new_file_name
#                 break
        
#         f = open(file_name, 'w+')
#         f.write('[]')
#         f.close()

#     return(file_name)

# def _json_writer(result_list: list, pathfile: str):
#     for item in result_list:
#         document = {
#             'title':item[0],
#             'url':item[1]
#         }

#         with open(pathfile) as reader:
#             data = json.load(reader)
#             data.append(document)
#         with open(pathfile, 'w') as writer:
#             json.dump(data, writer, indent=4)

#def _scrapper(term: str, pathfile: str):



def _scrapper(term: str):
    '''
    Bing scrapper, obtiene los resultados y los muestra por pantalla (Titulo y URL)
    '''

    user_agent = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0'
    }
    bing_url = f"https://www.bing.com/search?q={term}"
    result_list = []

    response = requests.get(bing_url, headers=user_agent)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    result_block = soup.select("li.b_algo > h2 > a")

    print(f"{term}:")
    for result in result_block:
        result_list.append([result.get_text(), result.get_attribute_list("href")])

    print(result_list)
 #   _json_writer(result_list, pathfile)



if __name__ == '__main__':
    main()