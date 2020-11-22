from django.contrib import admin
from blog.models import Category, Post

# Register your models here.

#두개를 어드민 사이트에 알려주는 것
admin.site.register(Category)
admin.site.register(Post)
