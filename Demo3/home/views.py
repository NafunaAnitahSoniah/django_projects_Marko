from django.shortcuts import render, redirect
from datetime import datetime

#box or list of the students
students = []

# Create your views here.
def homePage(request):
    if request.method == 'POST':
        #we are creating a variable in which we store the contents that we received from the POST method in the form
        form_data = request.POST 
        #We create a variable name that will capture the first field {student-name} from the form
        name = form_data['student_name']
        #We create a variable lucky_number that will capture the second field {lucky_number} from the form
        lucky_number = form_data['lucky_number']

        #below indicates what we want to do with the data received from the form
        new_student = {
            'name': name,
            'lucky_number': lucky_number
        }
        students.append(new_student)
    
        total_students = len(students)
        print("Total Students: " +str(total_students))
    
        return redirect('/')
    else:
        return render(request, "index.html", {"students":students})


"""
def addStudent(request):
    form_data = request.POST:
    name = form_data['student_name']
    lucky_number = form_data['lucky_number']
    new_student = {
        'name': name,
        'lucky_number': lucky_number
    }
    students.append(new_student)
"""

#creating a context and templating in django
def contextPage(request):
    context ={
        "name": "David",
        "date": datetime.now(),
        "students":21,
        
    }
    return render(request, "context.html", context)

def profilePage(request):
    age = 2025-1967
    context ={
        "name": "David",
        "nin_number":"CF2500GKMH",
        "course":"Math",
        #we can use a value or a variable
        "age":age, 
        
    }
    return render(request, "profile.html", context)

#Create a page that has a form so that a person is able to fill in the datad and they are able
# to fill in the data and they are able to get the response
# try to use A1 to give you challenges
# try to look up DYNAMIC URLS
