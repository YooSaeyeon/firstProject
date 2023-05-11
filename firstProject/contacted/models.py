from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=50, verbose_name='이름')
    email = models.EmailField(max_length=128, verbose_name='이메일')
    number = models.CharField(max_length=20, verbose_name='전화번호')
    body = models.TextField(verbose_name="내용", default="")
    
    def __str__(self):
        return self.name
    
    def __str__(self):
        return self.number