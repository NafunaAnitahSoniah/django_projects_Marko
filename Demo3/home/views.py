from django.shortcuts import render

#box or list of the students
students = []

# Create your views here.
def homePage(request):
    if request.method == 'POST':
        form_data = request.POST
        name = form_data['student_name']
        lucky_number = form_data['lucky_number']
        new_student = {
            'name': name,
            'lucky_number': lucky_number
        }
        students.append(new_student)
    
    total_students = len(students)
    print("Total Students: " +str(total_students))

    return render(request, "index.html")

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