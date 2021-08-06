import datetime

from django.contrib import admin
from django.db import models

# Create your models here.
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField('问题名', max_length=200)
    # pub_date = models.DateTimeField('date published')
    pub_date = models.DateTimeField('发布日期')

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        # description='Published recently?',
        description='是否最近发布',
    )
    def was_published_recently(self):
        now = timezone.now()
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    # 修改类名称
    class Meta:
        verbose_name = "问题"
        verbose_name_plural = "我的问题"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('投票选项', max_length=200)
    votes = models.IntegerField('投票数', default=0)

    def __str__(self):
        return self.choice_text

    # 修改类名称
    class Meta:
        verbose_name = "投票项"
        verbose_name_plural = "我的投票"
