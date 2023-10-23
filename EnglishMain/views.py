from django.shortcuts import render, redirect
from .models  import*
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request,'index.html')



def user_home(request):
    name = user_details.objects.filter(email=request.session['user_name'])
    course_details = category.objects.all()
    msg = {'msg1': name, 'course_cat': course_details}
    return render(request,'user_home.html', msg)



def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        reg_no = request.POST.get('reg_no')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        photo=request.FILES.get('photo')

        if user_details.objects.filter(email=email):
            msg = {'msg1' : 'Username already exits...!'}
            return render(request, 'signup.html', msg)
        else:


            ud = user_details(first_name=first_name, last_name =last_name, reg_no=reg_no, phone=phone, email=email, password=password,photo=photo )
            ud.save()
            # messages.success(request, 'Your profile is updated successfully!')
            return redirect('/login_page')

    else:
        return render(request, 'signup.html')


def login_page(request):
    if request.method == 'POST':

        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        ul = user_details.objects.filter(email=user_name, password=password)

        if ul.filter(email=user_name, password=password).exists():
            request.session['user_name'] = ul[0].email
            request.session["user_id"] = ul[0].id
            for i in ul:
                x = i.usertype
                request.session['usertype'] = x
            if x == 'A':
                for i in ul:
                    email = i.email
                    request.session['email'] = email
                    return redirect("/admin_panel/admin_home")
            elif x == 'User':
                for i in ul:
                    email = i.email
                    request.session['email']=email
                    print(request.session['email'])
                    return redirect("/user_home")
        else:
            # messages.success(request, 'login successfully!')
            msg = {'msg1': 'Invalid username or password....!'}
            return render(request, 'login_page.html', msg)

    else:
        return render(request, 'login_page.html')

def logout(request):

    try:
        del request.session['user_name']

        del request.session['user_id']
    except:
        return index(request)
    else:
        return render(request, 'index.html')

def course_details(request,pk):
    try:
        user_id = request.session['user_id']
        print(user_id)
        name = user_details.objects.filter(email=request.session['user_name'])
        t = category.objects.get(id=pk)
        cate = category.objects.filter(id=pk)
        d = course.objects.filter(cat=t)
        context = {'course_cat': d, 'msg1': name,'cat': cate}
        return render(request, 'course_details.html', context)
    except:
        return login_page(request)


def user_home(request):
    try:
        user_id = request.session['user_id']
        print(user_id)
        name = user_details.objects.filter(email=request.session['user_name'])
        course_details = category.objects.all()
        msg = {'msg1': name, 'course_cat': course_details}
        return render(request, 'user_home.html', msg)
    except:
        return login_page(request)

def user_profile(request):
    try:
        user_id = request.session['user_id']
        print(user_id)
        id = request.GET.get('id')
        user = user_details.objects.filter(id=int(id))
        context = {'details': user}
        return render(request, 'user_profile.html', context)
    except:
        return login_page(request)

def admin_profile(request):
    try:
        user_id = request.session['user_id']
        print(user_id)
        id = request.GET.get('id')
        user = user_details.objects.filter(id=int(id))
        context = {'details': user}
        return render(request, 'admin_profile.html', context)
    except:
        return login_page(request)

def admin_profile_edit(request):
    try:
        user_id = request.session['user_id']
        print(user_id)
        if request.method == 'POST':
            id = request.session['user_name']
            up = user_details.objects.get(email=id)
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            reg_no = request.POST.get('reg_no')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            if len(request.FILES) != 0:

                if len(up.photo) > 0:
                    os.remove(up.photo.path)
                up.photo = request.FILES['photo']



            up.first_name = fname
            up.last_name = lname
            up.reg_no = reg_no
            up.phone = phone

            up.save()
            ud = user_details.objects.filter(email=request.session['user_name'])
            context = {'details': ud}

            return render(request, 'admin_profile.html', context)


        else:
            id = request.GET.get('id')
            up = user_details.objects.filter(id=int(id))
            context = {'details': up}
            return render(request, 'admin_profile_edit.html', context)
    except:
        return login_page(request)
import os
def user_profile_edit(request):

    user_id = request.session['user_id']
    print(user_id)
    if request.method == 'POST':
        id = request.session['user_name']
        up = user_details.objects.get(email=id)
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        reg_no = request.POST.get('reg_no')
        phone = request.POST.get('phone')
        if len(request.FILES) != 0:

            if len(up.photo) > 0:
                os.remove(up.photo.path)
            up.photo = request.FILES['photo']


        up.first_name = fname
        up.last_name = lname
        up.reg_no = reg_no
        up.phone = phone


        up.save()
        ud = user_details.objects.filter(email=request.session['user_name'])
        context = {'details': ud}
        return render(request, 'user_profile.html', context)


    else:
        id = request.GET.get('id')
        up = user_details.objects.filter(id=int(id))
        context = {'details': up}
        return render(request, 'user_profile_edit.html', context)


def view_video(request,pk):
   
        print("reached")
        
        # Get the course with the given pk
        user_id=request.session["user_id"]
        course_object = course.objects.get(id=pk)
        cat=course_object.cat
        cat_id=cat.id
        print(cat_id)
        user=user_details.objects.get(id=user_id)

        # Check if the user has already viewed the video
        created=course_viewed.objects.filter(user=user, course=course_object).first()

        # If the user has not yet viewed the video, mark it as viewed
        if not created:
            view_obj = course_viewed(user=user, course=course_object)
            view_obj.save()
        url = f"/course_details/{ cat_id }"
        return redirect(url)


def user_changepassword(request):
    if request.method == 'POST':
        email=request.session['email']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print('Email Is:'+email)
        print("Current_password" + str(current_password))

        try:

            ul = user_details.objects.get(email=email,password=current_password)

            if ul is not None:
                ul.password = new_password  # change field
                ul.save()
                context = {'msg': 'Password Changed Successfully'}
                return render(request, 'user_changepassword.html', context)
            else:
                context = {'msg': 'Your Old Password is Wrong'}
                return render(request, 'user_changepassword.html', context)

        except user_details.DoesNotExist:
            context = {'msg': 'Your Old Password is Wrong'}
            return render(request, 'user_changepassword.html', context)
    else:
        return render(request, 'user_changepassword.html')


def admin_changepassword(request):
    if request.method == 'POST':
        email = request.session['email']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("Current_password" + str(current_password))

        try:

            ul = user_details.objects.get(email=email,password=current_password)

            if ul is not None:
                ul.password = new_password  # change field
                ul.save()
                context = {'msg': 'Password Changed Successfully'}
                return render(request, 'admin_changepassword.html', context)
            else:
                context = {'msg': 'Your Old Password is Wrong'}
                return render(request, 'admin_changepassword.html', context)

        except user_details.DoesNotExist:
            context = {'msg': 'Your Old Password is Wrong'}
            return render(request, 'admin_changepassword.html', context)
    else:
        return render(request, 'admin_changepassword.html')





def all_course(request):
    all = course.objects.all()
    context = {'all_course': all}
    return render(request, 'all_course.html', context)

def course_detail_page(request):
    id = request.GET.get('id')
    cat_id=request.GET.get('cat_id')
    print(cat_id)
    c = course.objects.filter(id=int(id))

    cat=category.objects.get(id=cat_id)
    print(cat)
    related=course.objects.filter(cat=cat)
    for i in related:
        print(i.title)


    context = {'course_detail': c, 'related' : related}
    return render(request, 'course_detail_page.html', context)
