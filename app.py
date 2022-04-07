from flask import Flask, request, render_template, send_from_directory
from functions import load_function_posts
from main.main import main_blueprint
from louder.louder import louder_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.register_blueprint(louder_blueprint)


@app.route("/uploads/images/<path:path>")
def static_on(path):
    return send_from_directory("uploads/images", path)


app.run(debug=True)
