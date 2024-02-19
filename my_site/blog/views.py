from datetime import date
from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountain",
        "image": "mountains.jpg",
        "author": "Maxmillian",
        "date": date(2021, 7, 22),
        "title": "Mountain hiking",
        "except": "There is nothing",
        "content": """Lorem ipsum doloar"""

    }
]

def get_date(post):
    return post['date']


# Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html",{
        "all_posts":all_posts
    })


def post_detail(request, slug):
    return render(request, "blog/post-detail.html")