from flask import Flask, render_template
import requests
from post import Post

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)
print(post_objects)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_posts=post_objects)

if __name__ == "__main__":
    app.run(debug=True)
