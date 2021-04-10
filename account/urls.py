from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'account'

urlpatterns = [
    # path('login/', views.user_login, name='user_login'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login2.html'), name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='user_logout'),
    path('register/', views.register, name='user_register'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='account/password_change_form.html',
                                                                   success_url="/account/password_change_done/"),
         name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'),
         name='password_change_done'),
    path('my-information/', views.myself, name='my_information'),

]