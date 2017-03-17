from django.shortcuts import render
from junge import models
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import auth
import datetime
from django_comments import models as comments_models
from django.template.context import RequestContext
# Create your views here.
def index(request):
    bbs_list=models.BBS.objects.all()
    user=request.user
    return  render(request,'index.html',locals())

def detail(request,d):
    bbs_obj=models.BBS.objects.get(id=d)

    return render(request,'bbs_detail.html',locals())

def sub_comment(request):
    bbs_id=request.POST.get('bbs_id')

    comment=request.POST.get('comment_content')
    c=comments_models.Comment()
    c.comment=comment
    c.object_pk=bbs_id
    c.content_type_id=7
    c.site_id=1
    c.user=request.user
    comments_models.Comment.save(c)

    return HttpResponseRedirect('/detail/%s' %bbs_id)

def acc_login(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        content='''
        Welcome %s !!!
        <a href='/logout/' >Logout</a>
        '''%user.username
        return HttpResponseRedirect('/')

def logout_view(request):
    user=request.user
    auth.logout(request)
    return HttpResponse("<b>%s</b> logge out! <br/><a href='/'>Re_login</a>" %user)
def Login(request):
    return render(request, 'zh.html')

def bbs_pub(request):

    return render(request,'bbs_pub.html')

def bbs_sub(request):
    author=models.BBS_user.objects.get(user__username=request.user)
    models.BBS.objects.create(
        title='test title',
    summary = 'haha',
    content = request.POST.get('content'),
    author = author,
    view_count = 1,
    ranking = 1,
    )
    return HttpResponse('yes.')

def reg(request):
    return render(request,'zhreg.html')


def log(request):
    return render(request,'zh.html')

def acc_reg(request):
    name=request.POST.get('username')
    pawd=request.POST.get('password')
    u=models.User(username=name)
    u.set_password(pawd)
    u.save()
    # obj=models.BBS_user.user
    #
    # obj.Username=name
    # obj.Password=pawd
    # obj.save()
    # obj=models.BBS_user.objects.get(user__username=request.user)
    # models.BBS_user.objects.create(
    #     Username=request.GET('username'),
    #     Password=request.GET('password'),
    # )
    # obj.username=request.GET('username')
    # obj.password=request.GET('password')
    # obj.save()
    return HttpResponse('注册成功！')
