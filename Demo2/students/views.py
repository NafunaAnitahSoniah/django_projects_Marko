from django.shortcuts import render

# Create your views here.
def calcHome(request):
    if request.method == 'POST':
        form_data = request.POST
        income_value = form_data['income']
        incometax = 30/100
        print('income')

    return render(request, "index.html")