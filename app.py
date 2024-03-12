from flask import Flask, render_template, request
from data import stories
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', stories=stories)

@app.route('/story')
def story():
    selected_slug = request.args.get('slug')
    selected_story = None
    for story in stories:
        if story['slug'] == selected_slug:
            selected_story = story
            break
    return render_template('str.html', selected_story=selected_story)

@app.route('/str_chap')
def str_chap():
    try:
        selected_slug = request.args.get('slug')
        selected_chap_index = int(request.args.get('chap_index'))
        selected_story = next((story for story in stories if story['slug'] == selected_slug), None)
        if selected_story:
            selected_chap = selected_story['chapters'][selected_chap_index]
            chapter_directory = os.path.join(selected_chap["image_directory"])
            images = [os.path.normpath(os.path.join(chapter_directory, image)) for image in os.listdir(chapter_directory) if image.endswith('.jpg')]
            # Sắp xếp các đường dẫn hình ảnh theo thứ tự số
            sorted_images = sorted(images, key=lambda x: int(''.join(filter(str.isdigit, x))))
            return render_template('str_chap.html', selected_story=selected_story, selected_chap=selected_chap, images=sorted_images, selected_chap_index=selected_chap_index)
        else:
            return "Truyện không tồn tại"
    except Exception as e:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
