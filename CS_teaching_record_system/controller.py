from Model.models import Course, Faculty, Teaches

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
def add_faculty(request):
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

def add_teaches(request):
    if request.POST:
        course_name = request.POST['course_name']
        faculty_name = request.POST['faculty_name']
        semester = request.POST['semester']

        faculty = Faculty.objects.filter(name=faculty_name)
        if faculty.exists():
            faculty_id = faculty.first()
        else:
            return HttpResponse("<p>faculty not found!!</p>")

        course = Course.objects.filter(name=course_name)
        if course.exists():
            course_id = course.first()
        else:
            return HttpResponse("<p>course not found!!</p>")

        teaches = Teaches(semester=semester,course=course_id,faculty=faculty_id)
        teaches.save()
        return HttpResponse("<p>Add Teaches Successfully!!</p>")
    else:
        return HttpResponse("<p>Add Teaches fail!!</p>")

def add_teaches_form(request):
    ctx = {}
    if 'faculty_name' in request.GET and request.GET['faculty_name']:
        ctx['faculty_name']=request.GET['faculty_name']
    if 'course_name' in request.GET and request.GET['course_name']:
        ctx['course_name']=request.GET['course_name']
    if 'semester' in request.GET and request.GET['semester']:
        ctx['semester']=request.GET['semester']
    return render(request, 'add_teaches.html',ctx)

def list_teaches(request):
    ctx = {}
    teaches_list = Teaches.objects.all()
    if 'course_name' in request.GET and request.GET['course_name']:
        course = Course.objects.get(name=request.GET['course_name'])
        teaches_list = teaches_list & course.teaches_set.all()

    if 'faculty_name' in request.GET and request.GET['faculty_name']:
        faculty = Faculty.objects.get(name=request.GET['faculty_name'])
        teaches_list = teaches_list & faculty.teaches_set.all()

    if 'semester' in request.GET and request.GET['semester']:
        teaches_list = teaches_list.filter(semester=request.GET['semester'])

    ctx['list'] = teaches_list

    return render(request,'list_teaches.html',ctx)

def delete_teaches(request):
    if 'teaches_id' in request.GET and request.GET['teaches_id']:
        teaches = Teaches.objects.get(id=int(request.GET['teaches_id']))
        teaches.delete()
        return HttpResponse("<p>Delete Teaches Successfully!!</p>")
    else:
        return HttpResponse("<p>Delete Teaches Failed!!</p>")

def list_free_faculty(request):
    ctx = {}
    faculty_list = Faculty.objects.all()
    teaches_list = Teaches.objects.all()
    if 'semester' in request.GET and request.GET['semester']:
        teaches_list = teaches_list.filter(semester=request.GET['semester'])
        ctx['semester'] = request.GET['semester']

    faculty_list = faculty_list.exclude(id__in=teaches_list.values_list('faculty',flat=True).distinct())

    ctx['list'] = faculty_list

    return render(request,'list_free_faculty.html',ctx)
