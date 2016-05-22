from django.db import models

ID2BOOKNAME = {
    '10001':'四级',
    '10002':'六级',
    '10003':'雅思',
    '10004':'托福'
}

ID2COUNT = {
    '20001':'2',
    '20002':'3',
    '20003':'4',
    '20004':'5',
    '20005':'10',
    '20006':'15',
    '20007':'20',
    '20008':'30',
    '20009':'40',
}

BOOKNAME2TYPE = {
    '四级':'is_4grade',
    '六级':'is_6grade',
    '雅思':'is_IELTS',
    '托福':'is_TOEFL'
}

class Words(models.Model):
    word = models.CharField(default=0,max_length=256)#单词
    meaning = models.TextField(blank = True, null = True)#单词释义
    synonym = models.CharField(blank = True,null = True,max_length=256)#同义词列表 [1,2,3]
    is_4grade = models.BooleanField(default=False)#是否是4级
    is_6grade = models.BooleanField(default=False)#是否是6级
    is_IELTS = models.BooleanField(default=False)#是否是雅思
    is_TOEFL = models.BooleanField(default=False)#是否是托福
    created_at = models.DateTimeField(auto_now_add=True, null=True)#创建时间

    def __str__(self):
        return self.word


    class Meta:
        db_table = 'Words'
        verbose_name = '词库'
        ordering = ['id']





