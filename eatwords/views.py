from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response

from core import jsonresponse,get_trace
from eatwords.models import EatwordsConfig,WordNote
from vocabulary.models import ID2BOOKNAME,ID2COUNT,BOOKNAME2TYPE,Words

@login_required()
def index(request):

    return render_to_response('index.html',{})

@login_required()
def eating(request):
    if request.POST.get('_method')=='put':
        user_id = str(request.user.id)
        bookId = request.POST.get('bookId','')
        countId = request.POST.get('countId','')
        book_name = ID2BOOKNAME(bookId)
        book_type = BOOKNAME2TYPE(book_name)

        filter_dict = {}
        filter_dict[book_type] = True
        try:
            words_data = Words.objects.filter(**filter_dict).order_by('id')
            words_ids = [str(word.id) for word in words_data]
            db_ids = ",".join(words_ids)

            user_config = EatwordsConfig(
                user_id=user_id,
                book_id=bookId,
                count_id=countId,
                db_ids=db_ids
            )
        except:
            get_trace.print_trace()

        data = {
            'url': '/eating/'
        }
        resp = jsonresponse.creat_response(200)
        resp.data = data
        return resp.get_response()
    else:
        return render_to_response('eating.html',{})