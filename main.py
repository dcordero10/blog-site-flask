from flask import Flask, render_template
import requests
from post import Post


app = Flask(__name__)
posts = Post()


@app.route('/')
def home():
    blog_url = "https://api.npoint.io/ed99320662742443cc5b"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)


@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/posts/<int:num>')
def get_post(num):
    for blog_post in posts.all_posts:
        if num == blog_post["id"]:
            title = blog_post["title"]
            subtitle = blog_post["subtitle"]
            body = blog_post["body"]
    return render_template("post.html", title=title, subtitle=subtitle, body=body)


if __name__ == "__main__":
    app.run(debug=True)
