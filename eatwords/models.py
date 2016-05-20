from django.db import models
from django.contrib.auth.models import Group,User
from account.models import UserProfile

class EatwordsConfig(models.Model):
    user_id = models.CharField(default=0,max_length=100)#用户id
    book_id = models.CharField(default=0,max_length=100)#单词书
    count_id = models.CharField(default=0,max_length=100)#每日个数
    progress = models.CharField(default=0,max_length=100)#用户进度 {book:book_id,progress:progress_id}
    ok_id = models.CharField(default=0,max_length=100)#用户完成书列表 [1,2,3]
    db_ids = models.TextField(blank = True, null = True)#用户当前书单词ids集合(用于分析用户数据)
    created_at = models.DateTimeField(auto_now_add=True, null=True)#创建时间

    def __str__(self):
        config = '[Config] user_id:{},book_id:{},count_id:{}'.format(self.user_id,self.book_id,self.count_id)
        return config
    class Meta:
        db_table = 'eartwords_config'
        verbose_name = '背单词配置'
        ordering = ['id']

class WordNote(models.Model):
    user_id = models.CharField(default=0,max_length=100)#用户id
    word_id = models.CharField(default=0,max_length=100)#单词id [1,2,3]
    note_content = models.TextField(blank = True, null = True)#用户单词笔记
    created_at = models.DateTimeField(auto_now_add=True, null=True)  # 创建时间


    def __str__(self):
        note = '[Note] user_id:{},word_id:{},note:{}'.format(self.user_id, self.word_id, self.note_content[:5])
        return note


    class Meta:
        db_table = 'word_note'
        verbose_name = '用户单词笔记'
        ordering = ['id']

