from django.shortcuts import render, redirect

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