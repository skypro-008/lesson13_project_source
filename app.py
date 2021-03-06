from flask import Flask, request, render_template, send_from_directory
# from functions import ...

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


@app.route("/")
def page_index():
    pass


@app.route("/tag")
def page_tag():
    pass


@app.route("/post", methods=["GET", "POST"])
def page_post_create():
    pass


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()

