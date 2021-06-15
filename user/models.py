from django.db import models


class User(models.Model):
    _id = models.CharField(max_length=128, verbose_name='아이디', unique=True)
    nickname = models.CharField(
        max_length=128, verbose_name='닉네임', unique=True)
    email = models.EmailField(verbose_name='이메일', unique=True)
    password = models.CharField(max_length=128, verbose_name='비밀번호')
    grade = models.CharField(verbose_name="사용자 등급", max_length=8,
                             choices=(('admin', '관리자'), ('user', '유저')))
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return self.nickname

    class Meta:
        db_table = 'my_user'
        verbose_name = '고객'
        verbose_name_plural = '고객'
