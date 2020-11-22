from django.shortcuts import render
from blog.models import Category, Post

# Create your views here.
#데이터를 불러옴 (어드민 사이트의 데이터 -cre: 내림차순으로 6개
def index(req):
    post_latest = Post.objects.order_by("creatDate")[:6]
    context = {
        "post_latest" : post_latest

    }

    return render(req, "index.html", context=context)


