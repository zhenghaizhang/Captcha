from django.urls import path
import user.views as views


urlpatterns = [
    # 用户登录界面
    path('', views.loginView, name='login'),
    path('success/', views.successView, name='success'),
    # 验证码验证API接口
    path('ajax_val', views.ajax_val, name='ajax_val'),
]