from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response


@login_required()
def index(request):
    return render_to_response('index.html',{})

@login_required()
def eating(request):
    return render_to_response('eating.html',{})