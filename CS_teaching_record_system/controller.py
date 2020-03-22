from Model.models import Course, Faculty, Teaches

from django.http import HttpResponse, JsonResponse, HttpResponseServerError
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import json
from django.forms.models import model_to_dict

#index page
def index(request):
    return render(request, 'index.html')

# Course related
@csrf_exempt
def add_course(request):
    if request.POST:
        name = request.POST['name']
        credits = request.POST['credits']
        sectionNum = request.POST['sectionNumber']
        description = request.POST['description']

        course = Course(name=name,credits=credits,sectionNumber=sectionNum,description=description)
        course.save()

        response = HttpResponse("Add course successfully!!")
    else:
        response = HttpResponseServerError("Add course failed!!")
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

def add_course_form(request):
    return render(request, 'add_course.html')

def list_course(request):
    course_list = Course.objects.all()
    d = []
    for i in course_list:
        d.append(model_to_dict(i))
    response = JsonResponse(d, safe=False)

    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

@csrf_exempt
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
        response = HttpResponse("Modify Course Information Successfully!!")
    else:
        response = HttpResponseServerError("Modify fail!!")
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

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
        response = HttpResponse("Delete Course Successfully!!")
    else:
        response = HttpResponseServerError("Delete Course Failed!!")
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response


# faculty related
@csrf_exempt
def add_faculty(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        research = request.POST['research']

        faculty = Faculty(name=name,email=email,research_area=research)
        faculty.save()

        response = HttpResponse("Add faculty successfully!!")
    else:
        response = HttpResponseServerError("Add faculty failed!!")
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

def add_faculty_form(request):
    return render(request, 'add_faculty.html')

def list_faculty(request):
    # ctx = {}
    # faculty_list = Faculty.objects.all()
    #
    # ctx['list'] = faculty_list
    #
    # return render(request,'list_faculty.html',ctx)
    faculty_list = Faculty.objects.all()
    d = []
    for i in faculty_list:
        d.append(model_to_dict(i))
    response = JsonResponse(d, safe=False)

    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

@csrf_exempt
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

        response = HttpResponse("Modify Faculty Information Successfully!!")
    else:
        response = HttpResponseServerError("Modify fail!!")

    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

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
        response = HttpResponse("Delete Faculty Successfully!!")
    else:
        response = HttpResponseServerError("Delete Faculty Failed!!")

    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

@csrf_exempt
def add_teaches(request):
    if request.POST:
        course_name = request.POST['course_name']
        faculty_name = request.POST['faculty_name']
        semester = request.POST['semester']

        faculty = Faculty.objects.filter(name=faculty_name)
        if faculty.exists():
            faculty_id = faculty.first()
        else:
            response = HttpResponseServerError("faculty not found!!")
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "*"
            return response

        course = Course.objects.filter(name=course_name)
        if course.exists():
            course_id = course.first()
        else:
            response = HttpResponseServerError("course not found!!")
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "*"
            return response

        teaches = Teaches(semester=semester,course=course_id,faculty=faculty_id)
        teaches.save()
        response = HttpResponse("Add Teaches Successfully!!")
    else:
        response = HttpResponseServerError("Add Teaches fail!!")

    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

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
    teaches_list = Teaches.objects.all()
    if 'course_name' in request.GET and request.GET['course_name']:
        course = Course.objects.get(name=request.GET['course_name'])
        teaches_list = teaches_list & course.teaches_set.all()

    if 'faculty_name' in request.GET and request.GET['faculty_name']:
        faculty = Faculty.objects.get(name=request.GET['faculty_name'])
        teaches_list = teaches_list & faculty.teaches_set.all()

    if 'semester' in request.GET and request.GET['semester']:
        teaches_list = teaches_list.filter(semester=request.GET['semester'])

    d = []
    for i in teaches_list:
        temp={}
        temp['id']=i.id
        temp['semester']=i.semester

        temp_course={}
        temp_course['name']=i.course.name
        temp_course['credits'] = i.course.credits
        temp_course['sectionNumber'] = i.course.sectionNumber
        temp_course['description'] = i.course.description
        temp['course']=temp_course

        temp_faculty={}
        temp_faculty['name']=i.faculty.name
        temp['faculty']=temp_faculty

        d.append(temp)
    response = JsonResponse(d, safe=False)

    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response


def delete_teaches(request):
    if 'teaches_id' in request.GET and request.GET['teaches_id']:
        teaches = Teaches.objects.get(id=int(request.GET['teaches_id']))
        teaches.delete()
        response = HttpResponse("Delete Teaches Successfully!!")
    else:
        response = HttpResponseServerError("Delete Teaches Failed!!")

    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

def list_free_faculty(request):
    faculty_list = Faculty.objects.all()
    teaches_list = Teaches.objects.all()
    if 'semester' in request.GET and request.GET['semester']:
        teaches_list = teaches_list.filter(semester=request.GET['semester'])

    faculty_list = faculty_list.exclude(id__in=teaches_list.values_list('faculty',flat=True).distinct())

    d = []
    for i in faculty_list:
        d.append(model_to_dict(i))
    response = JsonResponse(d, safe=False)

    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response
