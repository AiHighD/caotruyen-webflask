# code cao 1 chap truyen bang link
import requests
from bs4 import BeautifulSoup, SoupStrainer
import re
import os
from unidecode import unidecode

# ham lay ten chap
def get_chap_name(soup):
    chap_header = soup.find('h2', class_='mg-t-10')
    if chap_header:
        chap_name = chap_header.text.strip()
        print(chap_name)
        return chap_name
    else:
        print("Khong tim thay ten cua chap!.")
        return "Unknown_chap"
#ham lay ten truyen
def get_title_name(soup):
    title_header = soup.find('h1', class_='mg-t-15')
    if title_header:
        title_name = title_header.text.strip()
        print(title_name)
        return title_name
    else:
        print("Khong tim thay tieu de cua chap!.")
        return "Unknown_chap"
# ham download anh va luu vao thu muc 
def download_images(images, folder_path):
    for image in images:
        img_data = image['src']
        print(img_data)
        if not img_data.startswith("data:image"):
            filename = img_data.split('/')[-1]
            response = requests.get(img_data)
            with open(os.path.join(folder_path, filename), "wb") as file:
                file.write(response.content)

# ham xu ly ten tieng viet
def process_vietnamese_string(input_string):
    return unidecode(input_string).lower().replace(" ", "")

#ham check thu muc ton tai
def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def main():
    pageTarget = 'https://nhasachmienphi.com/doc-online/truyen-tranh-doremon-333102'
    page = requests.get(pageTarget)
    soup = BeautifulSoup(page.content, 'html.parser', parse_only=SoupStrainer('body'))

    images = soup.find_all("img", src=re.compile(r'^https://file\.'))
    folder_name = get_chap_name(soup)
    title = get_title_name(soup)
    processed_title = process_vietnamese_string(title)
    processed_chap = process_vietnamese_string(folder_name)
    folder_path = f'./download/{processed_title}_{processed_chap}'
    create_folder(folder_path)
    download_images(images, folder_path)

if __name__ == "__main__":
    main()