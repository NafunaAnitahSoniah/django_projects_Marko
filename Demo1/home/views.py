from django.shortcuts import render

# Create your views here.
def Aboutpage(request):
    return render(request, "about.html")

def Contact(request):
    return render(request, "Soniah_in_her_element.jpg")


