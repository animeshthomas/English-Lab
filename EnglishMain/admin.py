from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(user_details)
admin.site.register(course)
admin.site.register(category)
admin.site.register(course_viewed)