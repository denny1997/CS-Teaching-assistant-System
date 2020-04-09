from Model.models import Course, Faculty, Teaches, course, faculty

from django.http import HttpResponse, JsonResponse, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from django.db import connection

import json
from rake_nltk import Rake
from gensim.models import Word2Vec

# Course related
@csrf_exempt
def add_course(request):
    if request.POST:
        name = request.POST['name']
        credits = request.POST['credits']
        title = request.POST['title']
        description = request.POST['description']

        cursor = connection.cursor()
        cursor.execute("insert into model_course (name, credits, title, description) values (%s, %s, %s, %s);", [name, credits, title, description])
        cursor.close()
        # course = Course(name=name,credits=credits,sectionNumber=sectionNum,description=description)
        # course.save()

        response = HttpResponse("Add course successfully!!")
    else:
        response = HttpResponseServerError("Add course failed!!")
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

def list_course(request):
    cursor = connection.cursor()
    cursor.execute("select * from model_course")
    course_list = cursor.fetchall()
    cursor.close()
    # course_list = Course.objects.all()
    d = []
    for i in course_list:
        temp={}
        temp['id']=i[0]
        temp['name']=i[1]
        temp['credits']=i[2]
        temp['title']=i[3]
        temp['description']=i[4]
        d.append(temp)
        # d.append(model_to_dict(i))
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
        title = request.POST['title']
        description = request.POST['description']

        cursor = connection.cursor()
        cursor.execute("update model_course set name=%s,title=%s,credits=%s,description=%s where id=%s;", [name, title, credits, description, id])
        cursor.close()
        # course = Course.objects.get(id=int(id))
        #
        # course.name = name
        # course.credits = credits
        # course.sectionNumber = sectionNum
        # course.description = description
        # course.save()
        response = HttpResponse("Modify Course Information Successfully!!")
    else:
        response = HttpResponseServerError("Modify fail!!")
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response


def delete_course(request):
    if 'course_id' in request.GET and request.GET['course_id']:
        cursor = connection.cursor()
        cursor.execute("delete from model_course where id=%s;",[request.GET['course_id']])
        cursor.close()
        # course = Course.objects.get(id=int(request.GET['course_id']))
        # course.delete()
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
        title = request.POST['title']

        cursor = connection.cursor()
        cursor.execute(
            "insert into model_faculty (name, email, title) values (%s,%s,%s);",[name, email, title])
        cursor.close()
        # faculty = Faculty(name=name,email=email,research_area=research)
        # faculty.save()

        response = HttpResponse("Add faculty successfully!!")
    else:
        response = HttpResponseServerError("Add faculty failed!!")
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response


def list_faculty(request):
    # ctx = {}
    # faculty_list = Faculty.objects.all()
    #
    # ctx['list'] = faculty_list
    #
    # return render(request,'list_faculty.html',ctx)
    # faculty_list = Faculty.objects.all()
    # d = []
    # for i in faculty_list:
    #     d.append(model_to_dict(i))
    cursor = connection.cursor()
    cursor.execute("select * from model_faculty")
    faculty_list = cursor.fetchall()
    cursor.close()
    # course_list = Course.objects.all()
    d = []
    for i in faculty_list:
        temp = {}
        temp['id'] = i[0]
        temp['name'] = i[1]
        temp['email'] = i[2]
        temp['title'] = i[3]
        d.append(temp)
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
        title = request.POST['title']

        # faculty = Faculty.objects.get(id=int(id))
        #
        # faculty.name = name
        # faculty.email = email
        # faculty.research_area = research
        # faculty.save()
        cursor = connection.cursor()
        cursor.execute(
            "update model_faculty set name=%s,title=%s,email=%s where id=%s;",[name, title, email, id])
        cursor.close()
        response = HttpResponse("Modify Faculty Information Successfully!!")
    else:
        response = HttpResponseServerError("Modify fail!!")

    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response


def delete_faculty(request):
    if 'faculty_id' in request.GET and request.GET['faculty_id']:
        # faculty = Faculty.objects.get(id=int(request.GET['faculty_id']))
        # faculty.delete()
        cursor = connection.cursor()
        cursor.execute("delete from model_faculty where id=%s",[request.GET['faculty_id']])
        cursor.close()
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

        # faculty = Faculty.objects.filter(name=faculty_name)
        # if faculty.exists():
        #     faculty_id = faculty.first()
        cursor = connection.cursor()
        cursor.execute("select id from model_faculty where name=%s",[faculty_name])
        f = cursor.fetchall()
        if len(f)>0:
            faculty_id = f[0][0]
        else:
            response = HttpResponseServerError("faculty not found!!")
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "*"
            return response

        # course = Course.objects.filter(name=course_name)
        # if course.exists():
        #     course_id = course.first()
        cursor.execute("select id from model_course where name=%s", [course_name])
        c = cursor.fetchall()
        if len(c) > 0:
            course_id = c[0][0]
        else:
            response = HttpResponseServerError("course not found!!")
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "*"
            return response

        # teaches = Teaches(semester=semester,course=course_id,faculty=faculty_id)
        # teaches.save()
        cursor.execute("insert into model_teaches(semester, course_id, faculty_id) values(%s,%s,%s);",[semester,course_id,faculty_id])
        cursor.close()
        response = HttpResponse("Add Teaches Successfully!!")
    else:
        response = HttpResponseServerError("Add Teaches fail!!")

    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response


def list_teaches(request):
    query = "select * from model_teaches, model_course, model_faculty where model_teaches.course_id=model_course.id and model_teaches.faculty_id=model_faculty.id"
    para = []
    # teaches_list = Teaches.objects.all()
    if 'course_name' in request.GET and request.GET['course_name']:
        # course = Course.objects.get(name=request.GET['course_name'])
        # teaches_list = teaches_list & course.teaches_set.all()
        query += " and model_course.name=%s and model_course.title=%s"
        course_name, course_title =  request.GET['course_name'].split('/')
        para.append(course_name)
        para.append(course_title)

    if 'faculty_name' in request.GET and request.GET['faculty_name']:
        # faculty = Faculty.objects.get(name=request.GET['faculty_name'])
        # teaches_list = teaches_list & faculty.teaches_set.all()
        query += " and model_faculty.name=%s"
        para.append(request.GET['faculty_name'])

    if 'semester' in request.GET and request.GET['semester']:
        # teaches_list = teaches_list.filter(semester=request.GET['semester'])
        query += " and model_teaches.semester=%s"
        para.append(request.GET['semester'])

    # print(query)

    cursor = connection.cursor()
    cursor.execute(query, para)
    teaches_list = cursor.fetchall()
    cursor.close()
    # print(teaches_list)

    d = []
    for i in teaches_list:
        temp={}
        temp['id']=i[0]
        temp['semester']=i[1]

        temp_course={}
        temp_course['name']=i[5]
        temp_course['credits'] = i[6]
        temp_course['title'] = i[7]
        temp_course['description'] = i[8]
        temp['course']=temp_course

        temp_faculty={}
        temp_faculty['name']=i[10]
        temp_faculty['email']=i[11]
        temp_faculty['title']=i[12]
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
        # teaches = Teaches.objects.get(id=int(request.GET['teaches_id']))
        # teaches.delete()
        cursor = connection.cursor()
        cursor.execute("delete from model_teaches where id=%s", [request.GET['teaches_id']])
        cursor.close()
        response = HttpResponse("Delete Teaches Successfully!!")
    else:
        response = HttpResponseServerError("Delete Teaches Failed!!")

    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

def list_free_faculty(request):
    # faculty_list = Faculty.objects.all()
    # teaches_list = Teaches.objects.all()
    if 'semester' in request.GET and request.GET['semester']:
        # teaches_list = teaches_list.filter(semester=request.GET['semester'])
        query = "select * from model_faculty where model_faculty.id not in (select faculty_id from model_teaches where semester=%s)"
        para = [request.GET['semester']]
    # faculty_list = faculty_list.exclude(id__in=teaches_list.values_list('faculty',flat=True).distinct())
    else:
        query = "select * from model_faculty where model_faculty.id not in (select faculty_id from model_teaches)"
        para = []

    cursor = connection.cursor()
    cursor.execute(query, para)
    faculty_list = cursor.fetchall()
    cursor.close()

    d = []
    for i in faculty_list:
        # d.append(model_to_dict(i))
        temp = {}
        temp['id'] = i[0]
        temp['name'] = i[1]
        temp['email'] = i[2]
        temp['title'] = i[3]
        d.append(temp)
    response = JsonResponse(d, safe=False)

    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response


def get_enroll_data(request):
    if 'course_id' in request.GET and request.GET['course_id'] and 'course_title' in request.GET and request.GET['course_title']:
        records = course.objects.filter(classId=request.GET['course_id'], name=request.GET['course_title'])
        res = []
        for r in records:
            temp = {}
            temp['semester'] = r.semester
            temp['instructor'] = r.instructor
            temp['enrollNumber'] = r.enrollNumber
            res.append(temp)
        response = JsonResponse(res, safe=False)
    else:
        response = HttpResponseServerError("Get Enroll Data Failed!!")

    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response


def get_enroll_data_faculty(request):
    if 'faculty_name' in request.GET and request.GET['faculty_name']:
        records = course.objects.filter(instructor=request.GET['faculty_name'])
        res = []
        for r in records:
            temp = {}
            temp['semester'] = r.semester
            temp['classId'] = r.classId
            temp['name'] = r.name
            temp['enrollNumber'] = r.enrollNumber
            res.append(temp)
        response = JsonResponse(res, safe=False)
        print(res)
    else:
        response = HttpResponseServerError("Get Enroll Data Failed!!")

    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response


def get_area_data(request):
    if 'faculty_name' in request.GET and request.GET['faculty_name']:
        records = faculty.objects.filter(name=request.GET['faculty_name'])
        res = records[0].areas
        response = JsonResponse(res, safe=False)
    else:
        response = HttpResponseServerError("Get Area Data Failed!!")

    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response


def get_keywords_scores(request):
    if 'description' in request.GET and request.GET['description']:
        r = Rake()
        r.extract_keywords_from_text(request.GET['description'])
        res = []
        for score, word in r.get_ranked_phrases_with_scores():
            temp={}
            temp['name']=word
            temp['value']=score
            res.append(temp)
        response = JsonResponse(res, safe=False)
    else:
        response = HttpResponseServerError("Get Keywords Failed!!")

    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response


def get_recommendation(request):
    if 'description' in request.GET and request.GET['description']:
        model = Word2Vec.load('word2vec\\model.mdl')
        label = model.wv.index2word[:11]
        vocab = [word for word, Vocab in model.wv.vocab.items()]
        score = {}
        for i in label:
            score[i] = 0
        r = Rake()
        r.extract_keywords_from_text(request.GET['description'])
        for w in r.get_ranked_phrases():
            w = w.replace(" ", "-")
            if w in vocab:
                for i in label:
                    score[i] += model.wv.similarity(w, i)
        area = max(score, key=lambda x: score[x]).replace("-"," ").title().replace("And","and")
        records = faculty.objects(areas=area)
        res = {}
        res['label'] = area
        res['faculty'] = [r.name for r in records]
        response = JsonResponse(res, safe=False)
    else:
        # response = HttpResponseServerError("Get Keywords Failed!!")
        records = faculty.objects.all()
        res = {}
        res['label'] = 'None'
        res['faculty'] = [r.name for r in records]
        response = JsonResponse(res, safe=False)

    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response


def import_course_data(request):
    fp = open('data\course.json','r')
    courses = json.load(fp)
    courses.sort(key=lambda x:int(x['name'].split()[-1]))
    cursor = connection.cursor()
    count = 0
    for course in courses:
        cursor.execute("insert into model_course (name, credits, title, description) values (%s, %s, %s, %s);",
                       [course['name'], course['credits'], course['title'], course['description']])
        count+=1
    cursor.close()
    response = HttpResponse("Successfully import "+str(count)+" records!")
    return response

def import_faculty_data(request):
    fp = open('data\\faculty.json','r')
    faculties = json.load(fp)
    cursor = connection.cursor()
    count = 0
    for faculty in faculties:
        cursor.execute("insert into model_faculty (name, email, title) values (%s,%s,%s);",[faculty['name'], faculty['email'], faculty['title']])
        count+=1
    cursor.close()
    response = HttpResponse("Successfully import "+str(count)+" records!")
    return response

def import_teaches_data(request):
    fp = open('data\\teaches.json','r')
    teaches = json.load(fp)
    cursor = connection.cursor()
    count = 0
    for teach in teaches:
        cursor.execute("select id from model_faculty where name=%s", [teach['faculty']])
        f = cursor.fetchall()
        if len(f) > 0:
            faculty_id = f[0][0]
        else:
            response = HttpResponseServerError("faculty not found!! "+teach['faculty'])
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "*"
            return response

        cursor.execute("select id from model_course where title=%s and name=%s", [teach['title'],teach['name']])
        c = cursor.fetchall()
        if len(c) > 0:
            course_id = c[0][0]
        else:
            response = HttpResponseServerError("course not found!! "+teach['name'])
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "*"
            return response

        cursor.execute("insert into model_teaches(semester, course_id, faculty_id) values(%s,%s,%s);",
                       [teach['semester'], course_id, faculty_id])

        count+=1

    cursor.close()
    response = HttpResponse("Successfully import "+str(count)+" records!")
    return response

