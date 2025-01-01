from urllib.request import urlopen
from urllib.parse import quote

import json
from bs4 import BeautifulSoup


# Wikipedia API on getting the contents: 4 ways: https://www.mediawiki.org/wiki/API:Get_the_contents_of_a_page
# the two first return wikitext which seems to be very sophisitcated WikiMedia markup language, universally difficult to parse
# 3rd method returns html

core_url = 'https://en.wikipedia.org/w/api.php'
def get_request_parameters_stirng(page: str):
  # name =  page.encode('utf-8')
  return f'?action=parse&page={quote(page)}&prop=text&formatversion=2&format=json'


def get_page_content(page):

  print(page)
  url = f'{core_url}{get_request_parameters_stirng(page)}'
  response = urlopen(url)
  json_content = json.load(response)
  html_content = json_content["parse"]["text"]
  return html_content

def get_paragraphs(html_string:str):
  # preliminary cleaning
  cleared_html_string = html_string.replace("\n", "")
  soup = BeautifulSoup(cleared_html_string, 'html.parser')
  all_paragraphs = [paragraph.get_text() for paragraph in soup.find_all("p") if paragraph.get_text().strip() and len(paragraph.get_text().strip().split(" ")) > 1]
  return all_paragraphs


def get_data(page_name):
  # fetch page
  print(f'Getting page: {page_name}')
  html_string = get_page_content(page_name)

  # preprocess page
  paragraphs = get_paragraphs(html_string=html_string)
  print(f"{len(paragraphs)} paragraphs found")

  return paragraphs
