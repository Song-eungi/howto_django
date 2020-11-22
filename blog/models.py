from django.db import models
from django.urls import reverse
# Create your models here.

#글의 분류
class Category(models.Model):
    name = models.CharField(max_length=50, help_text="블로그 글의 분류를 입력하세요")
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name
#블로그 글 (제목, 작성일, 대표 이미지, 내용, 분류)
class Post(models.Model):
    title = models.CharField(max_length=200)
    title_image = models.ImageField(blank=True)
    content = models.TextField()
    creatDate = models.DateTimeField(auto_now_add=True)
    updatDate = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, help_text="글의 분류를 설정하세요")

    def __str__(self):
        return self.title

    #1번글의 경우 -> single/1로 자기자신을 찾아올수 잇는 주소를 알려주겠다
    def get_absolute_url(self):
        return reverse("single", args=[str(self.id)])

    def is_content_more300(self):
        return len(self.content) > 1000

    def get_content_under300(self):
        return self.content[:1000]

