from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30) # 길이 제한이 있는 문자열 (max_length가 30)
    content = models.TextField() # 길이 제한이 없는 문자열

    created_at = models.DateTimeField() # 생성된 날짜와 시각을 저장
    # author : 추후 작성 예정
