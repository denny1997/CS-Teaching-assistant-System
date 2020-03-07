from Model.models import Course, Faculty

from django.http import HttpResponse
from django.shortcuts import render

#index page
def index(request):
    return render(request, 'index.html')

# Course related
def add_course(request):
    if request.POST:
        name = request.POST['name']
        credits = request.POST['credits']
        sectionNum = request.POST['sectionNumber']
        description = request.POST['description']

        course = Course(name=name,credits=credits,sectionNumber=sectionNum,description=description)
        course.save()

        return HttpResponse("<p>Add course successfully!!</p>")
    else:
        return HttpResponse("<p>Add course failed!!</p>")

def add_course_form(request):
    return render(request, 'add_course.html')

def list_course(request):
    ctx = {}
    course_list = Course.objects.all()

    ctx['list'] = course_list

    return render(request,'list_course.html',ctx)

def modify_course(request):
    if request.POST:
        id = request.POST['id']
        name = request.POST['name']
        credits = request.POST['credits']
        sectionNum = request.POST['sectionNumber']
        description = request.POST['description']

        course = Course.objects.get(id=int(id))

        course.name = name
        course.credits = credits
        course.sectionNumber = sectionNum
        course.description = description
        course.save()
        return HttpResponse("<p>Modify Course Information Successfully!!</p>")
    else:
        return HttpResponse("<p>Modify fail!!</p>")

def modify_course_form(request):
    ctx = {}
    if 'course_id' in request.GET and request.GET['course_id']:
        course = Course.objects.get(id=int(request.GET['course_id']))
        ctx['modify_course']=course
        return render(request, 'modify_course.html', ctx)
    else:
        return HttpResponse("<p>Modify fail!!</p>")

def delete_course(request):
    if 'course_id' in request.GET and request.GET['course_id']:
        course = Course.objects.get(id=int(request.GET['course_id']))
        course.delete()
        return HttpResponse("<p>Delete Course Successfully!!</p>")
    else:
        return HttpResponse("<p>Delete Course Failed!!</p>")


# faculty related
def add_falculty(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        research = request.POST['research']

        faculty = Faculty(name=name,email=email,research_area=research)
        faculty.save()

        return HttpResponse("<p>Add faculty successfully!!</p>")
    else:
        return HttpResponse("<p>Add faculty failed!!</p>")

def add_faculty_form(request):
    return render(request, 'add_faculty.html')

def list_faculty(request):
    ctx = {}
    faculty_list = Faculty.objects.all()

    ctx['list'] = faculty_list

    return render(request,'list_faculty.html',ctx)

def modify_faculty(request):
    if request.POST:
        id = request.POST['id']
        name = request.POST['name']
        email = request.POST['email']
        research = request.POST['research']

        faculty = Faculty.objects.get(id=int(id))

        faculty.name = name
        faculty.email = email
        faculty.research_area = research
        faculty.save()
        return HttpResponse("<p>Modify Faculty Information Successfully!!</p>")
    else:
        return HttpResponse("<p>Modify fail!!</p>")

def modify_faculty_form(request):
    ctx = {}
    if 'faculty_id' in request.GET and request.GET['faculty_id']:
        faculty = Faculty.objects.get(id=int(request.GET['faculty_id']))
        ctx['modify_faculty']=faculty
        return render(request, 'modify_faculty.html', ctx)
    else:
        return HttpResponse("<p>Modify fail!!</p>")

def delete_faculty(request):
    if 'faculty_id' in request.GET and request.GET['faculty_id']:
        faculty = Faculty.objects.get(id=int(request.GET['faculty_id']))
        faculty.delete()
        return HttpResponse("<p>Delete Faculty Successfully!!</p>")
    else:
        return HttpResponse("<p>Delete Faculty Failed!!</p>")