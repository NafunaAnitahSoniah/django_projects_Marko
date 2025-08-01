from django.shortcuts import render, redirect
from StudentsHome.models import Student

# Create your views here.
def homePage(request):
    #This is the READ quesrry from CRUD
    all_students = Student.objects.all() 
    total_students = len(all_students)
  
   #calculating average mark
    total = 0
    for each in all_students:
        total = total + int(each.result)
    average = total/ total_students

    #counting male and female
    male = 0
    female = 0
    for each in all_students:
        if each.gender == 'male':
            male = male + 1
        else:
            female = female + 1
            

    context = {
        "all_students": all_students,
        "total": total_students,
        "average": average
    }
    return render(request, "home.html")

def addPage(request):
    if request.method == 'POST':
        form_data = request.POST
        #Get each form data 
        name = form_data['name']
        gender = form_data['gender']
        date_of_birth = form_data['date_of_birth']
        email = form_data['email']
        phone = form_data['phone']
        address = form_data['address']
        next_of_kin = form_data['next_of_kin']
        next_of_kin_phone = form_data['next_of_kin_phone']
        course = form_data['course']
        result = form_data['result']
        #generating an automatic student ID
        # all_students = Student.objects.all() 
        # total_students = len(all_students)
        # prefix = "ST2500_"+str(total_students + 1)
        student_id = form_data['student_id']

        #next, we shall initialise a student object using the student model
        #this is the CREATE querry from CRUD
        new_student = Student()
        new_student.names = name
        new_student.gender = gender
        new_student.date_of_birth = date_of_birth
        new_student.email = email
        new_student.phone = phone
        new_student.address = address
        new_student.next_of_kin = next_of_kin
        new_student.next_of_kin_phone = next_of_kin_phone
        new_student.course = course
        new_student.result = result
        new_student.student_id = student_id
        new_student.save() #commits the data to the database
        return redirect('/')

    return render(request, "add_stud.html")    

def viewPage(request, student_id):
    specific_student = Student.objects.filter(student_id=student_id)

    return render(request, "viewStudent.html")

def searchPage(request):
    if request.method == 'POST':
        form_data = request.POST
        query = form_data['query']
        #depending on the row to search
        results = Student.objects.filter(name_contains=query)
        total_results = results.count()
        all_students = Student.objects.all() 
       
        context = {
            "query": query,
            "total_results": total_results,
            "students": all_students,
        }
        return render(request, "search.html", context)

    return render(request, "search.html")