from django.shortcuts import render, redirect
from home.models import UserAccount

# Create your views here.
def Login(request):
    if request.method == 'POST':
        form_data = request.POST
        sentEmail = form_data['email']
        sentPassword = form_data['password']

        #to cross-check if the details provided by the user are in the database
        #Authentication
        selectedUser = UserAccount.objects.filter(
            email = sentEmail,
            password = sentPassword,
        )
        #django checks the database for the sent mail and password combination and returns an array
        if len(selectedUser) == 0:
            context = {
                #a message is displayed to the user in case their details are not in the database
                "message": "user not found" 
            }
            return render(request, "login.html", context)
        else:
            user = selectedUser[0] #
            role = user.role
            #to generate a cookie/ session that can be used to identify the user in each page they try to access
            request.session["userID"] = user.id 
            #to do: check each role and redirect them to a different page
            return redirect('/')

    return render(request, "login.html")

def customerPage(request):
    #to ensure that a user only accesses a page after they have logged in, if not direct them back to the login page
    # userID acts as a badge for the user trying to access a page
    userID = request.session.get("userID", None)
    if userID is None:
        return redirect('/login')

    return render(request, "index.html")

