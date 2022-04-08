import json

POST_PATH = "posts.json"


def load_function_posts():
    with open(POST_PATH, 'r', encoding='utf-8') as file:
        posts = json.load(file)
        return posts


def uploads(posts):
    with open(POST_PATH, 'w', encoding='utf-8') as file:
        json.dump(posts, file)
