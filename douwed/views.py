﻿from django.shortcuts import render_to_response, get_object_or_404
from info.forms import ContactForm
from info.models import UserDetail
from django.template import RequestContext
from social_auth.models import UserSocialAuth
from django.http import HttpResponseRedirect
import re
from django.contrib import auth
import json
import urllib2
value = range(1, 24)


def index(request):
    userdetail = UserDetail.objects.order_by('-id')
    title = "豆伴"
    return render_to_response("index.html", RequestContext(request, {'value': value, 'title': title, 'userdetail': userdetail}))


def about(request):
    id = request.user.id
    userdetail = get_object_or_404(UserDetail, user_id=id)
    return render_to_response("about.html", context_instance=RequestContext(request))


def reg(request):
    form = ContactForm()
    errors = []
    id = request.user.id
    userdetail = get_object_or_404(UserDetail, user_id=id)
    if request.method == 'POST':
        if not request.POST['position']:
            errors.append('请输入一个地址')
        if not request.POST['want_say']:
            errors.append('请输入你想对你另一半说的话')
        if not errors:
            userdetail.position = request.POST['position']
            userdetail.want_say = request.POST['want_say']
            userdetail.save()
    title = "在豆伴登记"
    return render_to_response("reg.html",
                              RequestContext(request, {'form': form, 'errors': errors, 'title': title, 'userdetail': userdetail}))


def logout(request):
    auth.logout(request)
    return render_to_response("logout.html")


def get_user_info(request):
    if request.method == 'GET':
        id = request.user.id
        userdetail = get_object_or_404(UserDetail, user_id=id)
        social_auth = get_object_or_404(UserSocialAuth, user=id)
        userdetail.uid = social_auth.uid
        userdetail.head_img = 'http://img3.douban.com/icon/u' + userdetail.uid + '.jpg'
        userdetail.extra = social_auth.extra_data
        resUser = urllib2.urlopen("https://api.douban.com/v2/user/" + userdetail.uid, timeout=10).read()
        jsonVal = json.loads(resUser)
        userdetail.user_name = jsonVal["name"]
        userdetail.head_img = jsonVal["avatar"]
        userdetail.save()
        print userdetail.user_name
        print userdetail.uid
    return HttpResponseRedirect('/')
