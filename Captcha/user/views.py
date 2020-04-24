from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import CaptchaTestForm
# 用户登录
def loginView(request):
    if request.method == 'POST':
        form = CaptchaTestForm(request.POST)
        # 验证表单数据
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if User.objects.filter(username=username):
                user = authenticate(username=username, password=password)
                if user:
                    if user.is_active:
                        login(request, user)
                        tips = '登录成功'
                        return redirect('/success/')
                else:
                    tips = '账号密码错误，请重新登录'
            else:
                tips = '用户不存在，请注册'
    else:
        form = CaptchaTestForm()
    return render(request, 'user.html', locals())


from django.http import JsonResponse
from captcha.models import CaptchaStore
# ajax接口，实现动态验证码
def ajax_val(request):
    if request.is_ajax():
        # 用户输入的验证码结果
        response = request.GET['response']
        # 隐藏的value值
        hashkey = request.GET['hashkey']
        cs = CaptchaStore.objects.filter(response=response, hashkey=hashkey)
        # 若cs存在，则验证成功
        if cs:
            json_data = {'status': 1}
        else:
            json_data = {'status': 0}
        return JsonResponse(json_data)
    else:
        json_data = {'status': 0}
        return JsonResponse(json_data)

def successView(request):
    return HttpResponse("登录成功！")