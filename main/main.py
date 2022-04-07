from flask import Flask, request, render_template, send_from_directory, Blueprint
from functions import load_function_posts
import logging

logging.basicConfig(encoding='utf-8', level=logging.INFO)

main_blueprint = Blueprint('main', __name__, template_folder="templates")


@main_blueprint.route('/')
def main():
    return render_template('index.html')


@main_blueprint.route('/search')
def search():
    search_by = request.args['s']
    logging.info(f"Было запрос на {search_by}")
    posts = [x for x in load_function_posts() if search_by.lower() in x['content'].lower()]
    return render_template('post_list.html', search_by=search_by, posts=posts)
