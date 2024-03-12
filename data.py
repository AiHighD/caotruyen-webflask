import os

# Thư mục chứa tất cả các thư mục chương
chapter_directory = "static/assets/images/chapters"

# Tạo danh sách các thư mục chứa hình ảnh cho mỗi chương
chapter_directories = [os.path.join(chapter_directory, d) for d in os.listdir(chapter_directory) if os.path.isdir(os.path.join(chapter_directory, d))]

# Hàm để lấy danh sách các thư mục chứa hình ảnh cho từng chương
def get_chapters(directory):
    return [{"image_directory": os.path.join(directory, f"chap{i+1}")}
            for i in range(50)]  # Số lượng chương

stories = [
    {
        "title": "One Piece",
        "slug": "one_piece",
        "image_path": "static/assets/images/one-piece.jpg",
        "description": "One Piece – Đảo Hải Tặc",
        "number_of_chapters": 25,
        "author": "Eiichiro Oda",
        "chapters": get_chapters("static/assets/images/chapters/one_piece")
    },
    {
        "title": "Naruto",
        "slug": "naruto",
        "image_path": "static/assets/images/naruto.jpg",
        "description": "Naruto",
        "number_of_chapters": 44,
        "author": "Masashi Kishimoto",
        "chapters": get_chapters("static/assets/images/chapters/naruto")
    },
    {
        "title": "Dragon Ball",
        "slug": "dragon_ball",
        "image_path": "static/assets/images/dragon-ball.jpg",
        "description": "Dragon Ball",
        "number_of_chapters": 27,
        "author": "Akira Toriyama",
        "chapters": get_chapters("static/assets/images/chapters/dragon_ball")
    },
    {
        "title": "Doremon Plus",
        "slug": "doremon_plus",
        "image_path": "static/assets/images/doremon-plus.jpg",
        "description": "Doremon Plus",
        "number_of_chapters": 26,
        "author": "Fujiko F. Fujio",
        "chapters": get_chapters("static/assets/images/chapters/doremon_plus")
    },
    {
        "title": "Doremon Truyện Dài",
        "slug": "doremon_truyen_dai",
        "image_path": "static/assets/images/doremon-truyen-dai.jpg",
        "description": "Doremon Truyện Dài",
        "number_of_chapters": 12,
        "author": "Fujiko F. Fujio",
        "chapters": get_chapters("static/assets/images/chapters/doremon_truyen_dai")
    },
    {
        "title": "Doremon Truyện Ngắn",
        "slug": "doremon_truyen_ngan",
        "image_path": "static/assets/images/doremon-truyen-ngan.jpg",
        "description": "Doremon Truyện Ngắn",
        "number_of_chapters": 8,
        "author": "Fujiko F. Fujio",
        "chapters": get_chapters("static/assets/images/chapters/doremon_truyen_ngan")
    },
    {
        "title": "Conan",
        "slug": "conan",
        "image_path": "static/assets/images/conan.jpg",
        "description": "Thám Tử Lừng Danh Conan",
        "number_of_chapters": 50,
        "author": "Gosho Aoyama",
        "chapters": get_chapters("static/assets/images/chapters/conan")
    },
    {
        "title": "Ô Long Viện",
        "slug": "o_long_vien",
        "image_path": "static/assets/images/o-long-vien.jpg",
        "description": "Ô Long Viện Siêu Buồn Cười",
        "number_of_chapters": 50,
        "author": "Au, Yao-hsing",
        "chapters": get_chapters("static/assets/images/chapters/o_long_vien")
    },
    {
        "title": "Tây Du",
        "slug": "tay_du",
        "image_path": "static/assets/images/tay-du.jpg",
        "description": "Truyện Tranh Tây Du",
        "number_of_chapters": 50,
        "author": "Trịnh Kiện Hoà - Đặng Chí Huy",
        "chapters": get_chapters("static/assets/images/chapters/tay_du")
    }
]
