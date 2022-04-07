from flask import Flask, request, render_template, send_from_directory, Blueprint
from functions import load_function_posts, uploads
import logging

logging.basicConfig(encoding='utf-8', level=logging.INFO)

louder_blueprint = Blueprint('louder_blueprint', __name__, url_prefix='/post', static_folder='static',
                             template_folder='templates')


@louder_blueprint.route('/form/')
def form():
    return render_template('post_form.html')


@louder_blueprint.route('/upload/', methods=["POST"])
def load(content=None):
    try:
        file = request.files['picture']
        file_name = file.filename
        posts = load_function_posts()
        content = request.values['content']
        posts.append({
            'pic': f'uploads/images/{file_name}',
            'content': content
        })
        uploads(posts)
        file.save(f'uploads/images/{file_name}')
        if file_name.split('.')[-1] not in ['png', 'img', 'jpeg']:
            logging.info("Файл не картинка")
    except FileNotFoundError:
        return "<h1> Ошибка, файла не существует </h1> "
    else:
        return render_template('post_uploaded.html', pic=f"/uploads/images/{file_name}", content=content)
