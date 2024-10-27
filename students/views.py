from django.shortcuts import render
import random

def generate_students():
    students_list = []
    names = ['nika', 'sandro', 'luka', 'giorgi', 'ana']
    surnames = ['pkhakadze', 'giorgadze', 'gvelesiani', 'ckhaidze', 'wulukidze']
    courses = ['python', 'javascript', 'java', 'c#']

    for i in range(0,101):
        name = random.choice(names)
        surname = random.choice(surnames)
        gpa = round(random.uniform(1.0, 4.0), 2) 
        course = random.choice(courses)

        student = {
            'name': name,
            'surname': surname,
            'gpa': gpa,
            'course': course,
        }
        students_list.append(student)

    return students_list


def main_page_view(request):
    student = random.choice(generate_students())
    return render(request,'mainpage.html', {'students': student})

def students_page_view(request):
    students = generate_students()
    return render(request,"students.html", {"students": students})

                                                                                                                                                                                    