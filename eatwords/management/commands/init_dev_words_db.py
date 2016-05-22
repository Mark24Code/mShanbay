from django.core.management.base import BaseCommand, CommandError
from vocabulary.models import Words
class Command(BaseCommand):
    help = '填充开发单词库'

    def handle(self, *args, **options):
        Words.objects.all().delete()
        print("生成开发词库...")
        dev_words = []
        #四级
        for i in range(20):
            dev_words.append(
                Words(
                    word='G4'+str(i),
                    meaning='meaning'+str(i),
                    synonym="1,2",
                    is_4grade=True,
                    is_6grade=False,
                    is_IELTS=False,
                    is_TOEFL=False
                ))
        #六级
        for i in range(30):
            dev_words.append(
                Words(
                    word='G6'+str(i),
                    meaning='meaning'+str(i),
                    synonym="1,2",
                    is_4grade=False,
                    is_6grade=True,
                    is_IELTS=False,
                    is_TOEFL=False
                ))
        #雅思
        for i in range(20):
            dev_words.append(
                Words(
                    word='IELTS'+str(i),
                    meaning='meaning'+str(i),
                    synonym="1,2",
                    is_4grade=False,
                    is_6grade=False,
                    is_IELTS=True,
                    is_TOEFL=False
                ))
        #托福
        for i in range(15):
            dev_words.append(
                Words(
                    word='TOEFL'+str(i),
                    meaning='meaning'+str(i),
                    synonym="1,2",
                    is_4grade=False,
                    is_6grade=False,
                    is_IELTS=False,
                    is_TOEFL=True
                ))
        Words.objects.bulk_create(dev_words)
        print("词库准备完毕。")