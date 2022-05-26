from django.urls import path, reverse_lazy
from . import views
from blog.forms import LoginForm, PasswordChangeForm, UserRegisterForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('login/', LoginView.as_view(template_name='blog/login.html', form_class=LoginForm), name='login'),
    path('register/', views.register, name = 'register'), 
]