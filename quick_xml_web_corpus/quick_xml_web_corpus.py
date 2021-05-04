#!/usr/lib/python3.8
# -*-coding:utf-8 -*

"""
Alexander DELAPORTE - CRLAO
https://tekipaki.hypotheses.org/
https://github.com/alxdrdelaporte
https://gitlab.com/alxdrdelaporte

Minimal webscraping to create a text corpus (XML)
https://tekipaki.hypotheses.org/1758

INPUT
List of URL
OUTPUT
XML text corpus

Example URL list references =
* ウィキペディアの執筆者，2021，「YOSAKOI」『ウィキペディア日本語版』，（2021年4月29日取得，
https://ja.wikipedia.org/w/index.php?title=YOSAKOI&oldid=81215417）．
* ウィキペディアの執筆者，2021，「YOSAKOIソーラン祭り」『ウィキペディア日本語版』，（2021年4月29日取得，
https://ja.wikipedia.org/w/index.php?title=YOSAKOI%E3%82%BD%E3%83%BC%E3%83%A9%E3%83%B3%E7%A5%AD%E3%82%8A&oldid=83172556）．
* ウィキペディアの執筆者，2020，「鳴子 (音具)」『ウィキペディア日本語版』，（2021年4月29日取得，
https://ja.wikipedia.org/w/index.php?title=%E9%B3%B4%E5%AD%90_(%E9%9F%B3%E5%85%B7)&oldid=75878711）
* ウィキペディアの執筆者，2021，「よさこい祭り」『ウィキペディア日本語版』，（2021年4月29日取得，
https://ja.wikipedia.org/w/index.php?title=%E3%82%88%E3%81%95%E3%81%93%E3%81%84%E7%A5%AD%E3%82%8A&oldid=81203786）．
"""

import requests
from bs4 import BeautifulSoup as soup
import xml.etree.ElementTree as ET

url_list = ["https://ja.wikipedia.org/wiki/YOSAKOI",
            "https://ja.wikipedia.org/wiki/YOSAKOI%E3%82%BD%E3%83%BC%E3%83%A9%E3%83%B3%E7%A5%AD%E3%82%8A",
            "https://ja.wikipedia.org/wiki/%E9%B3%B4%E5%AD%90_(%E9%9F%B3%E5%85%B7)",
            "https://ja.wikipedia.org/wiki/%E3%82%88%E3%81%95%E3%81%93%E3%81%84%E7%A5%AD%E3%82%8A"]

root = ET.Element("CORPUS")
id = 1

for url in url_list:
    page = ET.SubElement(root, "Page")
    page.set("id", f"{id}")
    id += 1
    page_url = ET.SubElement(page, "URL")
    page_url.text = url
    page_text = ET.SubElement(page, "Text")
    page_text.text = soup(requests.get(url).text, "html.parser").text

xml_output = ET.tostring(root, encoding="unicode", method="xml")
pretty_xml = soup(xml_output, "xml").prettify()
with open("web_corpus.xml", "w", encoding="utf-8", errors="replace", newline="") as target:
    target.write(pretty_xml)
