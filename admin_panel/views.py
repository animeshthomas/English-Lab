from django.forms import modelform_factory
from django.shortcuts import get_object_or_404, render, redirect
from EnglishMain.models import *
from EnglishMain.views import *


# Create your views here.
def index(request):
    return render(request, 'admin_home.html')


def category_add(request):
    try:
        user_id = request.session['user_id']
        print(user_id)
        if request.method == "POST":
            name = request.POST["name"]
            image = request.FILES["image"]
            cat = category.objects.create(name=name, image=image)
            cat.save()
            cat = category.objects.all()
            context = {'msg1':name}
            url = '/admin_panel/category-all'
            return redirect(url)
        else:
            name = user_details.objects.filter(email=request.session['user_name'])
            context = {'msg1': name}
            return render(request, 'admin_add_category.html',context)
    except:
        return login_page(request)


def category_all(request):
    try:
        user_id = request.session['user_id']
        print(user_id)
        name = user_details.objects.filter(email=request.session['user_name'])
        cat = category.objects.all()
        context = {'categorys': cat,'msg1':name}
        return render(request, 'admin_all_category.html', context)
    except:
        return login_page(request)


def category_edit(request, pk):
    try:
        name = user_details.objects.filter(email=request.session['user_name'])
        user_id = request.session['user_id']
        print(user_id)
        cat = category.objects.get(id=pk)
        if request.method == "POST":
            name = request.POST["name"]
            if 'image' in request.FILES:
                image = request.FILES["image"]
            else:
                image = cat.image
            cat.name = name

            cat.image = image
            cat.save()
            url = '/admin_panel/category-all'
            return redirect(url)

        else:
            context = {'category': cat,'msg1':name}
            return render(request, 'category-edit.html', context)
    except:
        return login_page(request)


def category_delete(request, pk):
    try:
        user_id = request.session['user_id']
        print(user_id)
        cat = category.objects.get(id=pk)
        cat.delete()
        url = '/admin_panel/category-all'
        return redirect(url)
    except:
        return login_page(request)


def choose_category(request):
    try:
        name = user_details.objects.filter(email=request.session['user_name'])
        user_id = request.session['user_id']
        print(user_id)
        cat = category.objects.all()
        context = {'categorys': cat,'msg1':name}

        return render(request, 'choose_category.html', context)
    except:
        return login_page(request)


def category_course(request, pk):
    try:
        user_id = request.session['user_id']
        print(user_id)
        cat = category.objects.get(id=pk)
        chap = course.objects.filter(cat=cat)
        context = {'courses': chap, 'cat': cat}
        return render(request, 'category-course.html', context)
    except:
        return login_page(request)


def course_add(request, pk):
    try:
        user_id = request.session['user_id']
        print(user_id)
        if request.method == "POST":
            cat = category.objects.get(id=pk)

            name = request.POST["title"]
            desc = request.POST["description"]
            video = request.FILES["video"]
            thumb = request.FILES["image"]
            c = course.objects.create(title=name, description=desc, video=video, thumbnail=thumb, cat=cat)
            c.save()
            url = f"/admin_panel/category-course/{pk}"
            return redirect(url)



        else:
            cat = category.objects.get(id=pk)
            context = {'cat': cat}
            return render(request, 'admin_add_course.html', context)
    except:
        return login_page(request)


def course_edit(request, pk):
    try:
        user_id = request.session['user_id']
        print(user_id)
        cour = course.objects.get(id=pk)
        if request.method == "POST":
            name = request.POST["title"]
            desc = request.POST["description"]
            cour.title = name
            cour.description = desc
            if 'image' in request.FILES:
                image = request.FILES["image"]
                cour.thumbnail = image
            if 'video' in request.FILES:
                video = request.FILES["video"]
                cour.video = video
            cat = cour.cat
            cat_id = cat.id
            cour.save()
            url = '/admin_panel/category-all'
            url = f"/admin_panel/category-course/{cat_id}"
            return redirect(url)
        else:
            context = {'course': cour}
            return render(request, 'course-edit.html', context)
    except:
        return login_page(request)


def course_delete(request, pk):
    try:
        user_id = request.session['user_id']
        print(user_id)
        cou = course.objects.get(id=pk)
        cat = cou.cat
        cat_id = cat.id
        cou.delete()

        url = f"/admin_panel/category-course/{cat_id}"
        return redirect(url)

    except:
        return login_page(request)


def view_all_users(request):
    try:
        name = user_details.objects.filter(email=request.session['user_name'])
        user_id = request.session['user_id']
        print(user_id)
        userData = user_details.objects.all()
        context = {'userData': userData,'msg1':name}
        return render(request, 'view_all_users.html', context)
    except:
        return login_page(request)


def view_user_watchlist(request, pk):
    try:
        user_id = request.session['user_id']
        print(user_id)
        user = user_details.objects.get(id=pk)
        courses = course_viewed.objects.filter(user=user)
        context = {
            'user': user,
            'courses': courses
        }
        return render(request, 'view_user_watchlist.html', context)
    except:
        return login_page(request)


def all_videos(request):
    try:
        name = user_details.objects.filter(email=request.session['user_name'])
        user_id = request.session['user_id']
        print(user_id)
        courses = course.objects.all()
        context = {
            'courses': courses,'msg1':name
        }
        return render(request, 'view_all_courses.html', context)
    except:
        return login_page(request)


def view_viewers(request, pk):
    try:
        user_id = request.session['user_id']
        print(user_id)
        courses = course.objects.get(id=pk)
        viewed_courses = course_viewed.objects.filter(course=courses)
        context = {
            'courses_viewed': courses,
            'viewed_courses': viewed_courses,
        }

        return render(request, 'view_all_video_users.html', context)
    except:
        return login_page(request)

def admin_home(request):
    try:
        user_id = request.session['user_id']
        print(user_id)
        name = user_details.objects.filter(email=request.session['user_name'])
        course_details = category.objects.all()
        msg = {'msg1': name, 'course_cat': course_details}
        return render(request, 'admin_home.html', msg)
    except:
        return login_page(request)