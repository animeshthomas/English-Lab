from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('/category-add', category_add, name="category-add"),
    path('/category-all', category_all, name="category-all"),
    path('/category-edit/<int:pk>', category_edit, name="category-edit"),
    path('/category-delete/<int:pk>', category_delete, name="category-delete"),
    path('/choose-category', choose_category, name="choose-category"),
    path('/category-course/<int:pk>', category_course, name="category-course"),
    path('/course-add/<int:pk>', course_add, name="course-add"),
    path('/course-edit/<int:pk>', course_edit, name="course-edit"),
    path('/course-delete/<int:pk>', course_delete, name="course-delete"),
    path('/view_users',view_all_users,name="view_all_users"),
    path('/view_watchlist/<int:pk>',view_user_watchlist,name="view_user_watchlist"),
    path('/all_videos',all_videos,name="all_videos"),
    path('/view_viewers/<int:pk>',view_viewers,name="view_viewers"),
    path('/admin_home', admin_home, name="admin_home"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
