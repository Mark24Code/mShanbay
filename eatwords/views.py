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
        book_name = ID2BOOKNAME[bookId]
        book_type = BOOKNAME2TYPE[book_name]

        filter_dict = {}
        filter_dict[book_type] = True
        try:
            words_data = Words.objects.filter(**filter_dict).order_by('id')
            db_words_ids = [str(word.id) for word in words_data]
            db_ids = ",".join(db_words_ids)

            EatwordsConfig.objects.create(
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
    elif request.GET.get('_method')=='get':
        #基础
        user_id = str(request.user.id)
        user_config  = EatwordsConfig.objects.filter(user_id=user_id)[-1]#这里要处理一下边界

        count_id = user_config.count_id
        count = ID2COUNT[count_id]
        progress = user_config.progress

        collect = user_config.collect
        collect_words_ids = collect.split(',') if collect else []

        db_ids = user_config.db_ids
        db_words_ids = db_ids.split(',') if db_ids else []

        if progress:
            index = int(db_words_ids.index(progress))
        else:
            index = 0
        end = index+int(count)
        today_words_ids = db_words_ids[index:end] if db_words_ids else []
        cur_collect_words_ids = collect_words_ids and today_words_ids
        #Words DB Data
        id2words = {}
        all_words = Words.objects.all()
        for word in all_words:
            id2words[str(word.id)] = word.word

        today_words = all_words.filter(id__in=today_words_ids)

        word_id2synoym_ids = {}
        for word in today_words:
            if word.synonym:
                word_id2synoym_ids[str(word.id)] = word.synonym.split(',')
            else:
                word_id2synoym_ids[str(word.id)] = None
        
        word_id2synoym = {}
        for word_id in word_id2synoym_ids:
            synoym_ids = word_id2synoym_ids[word_id]
            if synoym_ids:
                for synoym_id in synoym_ids:
                    if word_id in word_id2synoym:
                        word_id2synoym[word_id].append(id2words[synoym_id])
                    else:
                        word_id2synoym[word_id] = [id2words[synoym_id]]
            else:
                word_id2synoym[word_id] = None

        #组织data
        items = []
        for word in today_words:
            word_id = str(word.id)
            items.append({
                'id':word_id,
                'meaning':word.meaning,
                'is_collect':True if word_id in cur_collect_words_ids else False,
                'synonym':word_id2synoym[word_id]
            })

        resp = jsonresponse.creat_response(200)
        data = {
            'items':items,
        }
        resp.data = data
        return resp.get_response()
    else:
        return render_to_response('eating.html',{})

# #Note DB Data
# share_notes = WordNote.objects.filter(word_id__in=today_words_ids,is_shared=True,is_used=True)
# note_ids = [str(note.id) for note in share_notes]
# word_id2notes = {}
# for note in share_notes:
#     note_dict = {}
#     note_dict['user_id'] = note.user_id
#     note_dict['word_id'] = note.word_id
#     note_dict['note_content'] = note.note_content
#
#     if note.user_id in word_id2notes:
#         word_id2notes[note.user_id].append(note_dict)
#     else:
#         word_id2notes[note.user_id] = [note_dict]
