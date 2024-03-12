# code cao nhieu chap, tuy chinh so chap cao
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
        print("Khong tim thay tieu de cua chap!.")
        return "Unknown_chap"

#ham lay ten truyen
def get_title_name(soup):
    title_header = soup.find('h1', class_='mg-t-15')
    if title_header:
        title_name = title_header.text.strip()
        print(title_name)
        return title_name
    else:
        print("Khong tim thay tieu de cua truyen!.")
        return "Unknown_title"

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
#ham check neu chua co thu muc thi tao
def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

# ham tang so cuoi cung moi url
def increase_last_number(url):
    # Tìm và tách số cuối cùng từ URL
    match = re.search(r'(\d+)$', url)
    if match:
        last_number = int(match.group(1))
        increased_number = last_number + 1
        # Thay thế số cuối cùng trong URL bằng số đã tăng
        new_url = re.sub(r'\d+$', str(increased_number), url)
        return new_url
    else:
        return None

# ham kiem tra url co ton tai hay khong
def url_exists(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

# ham ghi url da duoc tai vao file
def write_downloaded_urls(url):
    with open(downloaded_urls_file, "a") as file:
        file.write(url + "\n")
# main
def main():
    # Đường dẫn đến file chứa các liên kết
    base_urls = "base_url.txt"

    # Mở file và đọc các liên kết
    with open(base_urls, "r") as file:
        urls = file.readlines()

    # Dem so lan tai xuong
    downloaded_count = 0

    # Lặp qua từng URL
    for url in urls:
        url = url.strip()  # Loại bỏ khoảng trắng và ký tự xuống dòng
        # Lặp lại cho đến khi đạt được mục tiêu
        while downloaded_count < 25: # lap lai x lan, download x chap truyen (neu co)
            # Tăng số cuối cùng của URL cho lần lặp tiếp theo
            new_url = increase_last_number(url)
            if new_url is None:
                print("Không thể tăng số cuối cùng của URL.")
                break

            # Kiểm tra xem URL đã được tải xuống trước đó hay không
            with open(downloaded_urls_file, "r") as file:
                downloaded_urls = file.readlines()
            if new_url + "\n" in downloaded_urls:
                print(f"URL {new_url} đã được tải xuống trước đó.")
                url = new_url
                continue

            # kiem tra xem url co ton tai hay khong
            if not url_exists(new_url):
                print(f"URL {new_url} không tồn tại hoặc không thể truy cập.")
                break

            # Tien hanh tai xuong va luu anh
            page = requests.get(new_url)
            soup = BeautifulSoup(page.content, 'html.parser', parse_only=SoupStrainer('body'))

            # vi file anh truyen co dinh dang ban dau la https://file/... .jpg nen lay ra cac file co bat dau tu https://file/
            images = soup.find_all("img", src=re.compile(r'^https://file\.'))
            #lay ten chap
            folder_name = get_chap_name(soup)
            # lay ten truyen
            title = get_title_name(soup)
            # chuyen ten chap, truyen thanh dang chu thuong, khong dau
            processed_title = process_vietnamese_string(title)
            processed_chap = process_vietnamese_string(folder_name)
            # luu vao download
            folder_path = f'./download/{processed_title}_{processed_chap}'
            create_folder(folder_path)
            download_images(images, folder_path)

            # Tăng biến đếm lên 1
            downloaded_count += 1
            # Ghi URL vào file đã tải xuống
            write_downloaded_urls(new_url)
            # Cập nhật URL cho lần lặp tiếp theo
            url = new_url
            # up file len hadoop
        else:
            break
        
if __name__ == "__main__":
    downloaded_urls_file = "downloaded_urls.txt"
    main()


