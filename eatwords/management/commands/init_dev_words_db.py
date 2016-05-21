from django.core.management.base import BaseCommand, CommandError
from vocabulary.models import Words
class Command(BaseCommand):
    help = '填充开发单词库'

    def handle(self, *args, **options):
        dev_words = []
        for i in range(20):
            dev_words.append(
                Words(
                    word='a'+str(i),
                    meaning='meaning'+str(i),
                    synonym="1,2",
                    is_4grade=True,
                    is_6grade=False,
                    is_IELTS=False,
                    is_TOEFL=False
                ))
        print(dev_words)
        Words.objects.bulk_create(dev_words)

