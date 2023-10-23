from .views import *
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',index,name="index"),
    path('signup',signup,name="signup"),
    path('login_page',login_page,name="login_page"),
    path('logout',logout,name="logout"),
    path('user_home', user_home, name="user_home"),
    path('all_course', all_course, name="all_course"),
    path('course_detail_page', course_detail_page, name="course_detail_page"),
    path('admin_profile_edit', admin_profile_edit, name="admin_profile_edit"),
    path('admin_changepassword', admin_changepassword, name="admin_changepassword"),

    path('course_details/<int:pk>', course_details, name="course_details"),
    path('mark_video_viewed/<int:pk>',view_video,name='mark_video_viewed'),
    # path('tutorials', views.tutorials, name="tutorials"),
    path('user_profile', user_profile, name="user_profile"),
    path('user_profile_edit', user_profile_edit, name="user_profile_edit"),
    path('user_changepassword', views.user_changepassword, name='user_changepassword'),

    path('admin_profile', admin_profile, name="admin_profile"),

]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)