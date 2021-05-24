import requests
class Post:
    def __init__(self):
        blog_url = "https://api.npoint.io/ed99320662742443cc5b"
        response = requests.get(blog_url)
        self.all_posts = response.json()