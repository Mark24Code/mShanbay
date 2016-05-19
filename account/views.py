import traceback
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.shortcuts import render,render_to_response
from django.template import RequestContext

from core import jsonresponse,get_trace
from account.models import UserProfile

def login(request):
    """登录"""
    # 注册
    if request.POST.get('_method', '') == 'put':
        pass
    #     username = request.POST.get('username', '')
    #     password = request.POST.get('password', '')
    #     try:
    #         user = User.objects.create_user(username=username, password=password)
    #         profile = UserProfile(
    #             user_id=str(user.id),
    #             nickname=username
    #         )
    #         profile.save()
    #     except:
    #         get_trace.print_trace()
    #
    #     resp = jsonresponse.creat_response(200)
    #     data = {
    #         'url': '/login/'
    #     }
    #     resp.data = data
    #     return resp.get_response()
    # # 登录
    # elif request.POST.get('_method', '') == 'post':
    #     username = request.POST.get('username', '')
    #     password = request.POST.get('password', '')
    #     user = auth.authenticate(username=username, password=password)
    #     if user and user.is_active:
    #         auth.login(request, user)
    #         request.session['user_id'] = user.id
    #         data = {
    #             'url': reload_url
    #         }
    #         resp = jsonresponse.creat_response(200)
    #         resp.data = data
    #         return resp.get_response()
    else:
        return render_to_response('login.html', {})

def logout(request):
    return render_to_response('logout.html',{})

def join(request):
    return render_to_response('join.html',{})