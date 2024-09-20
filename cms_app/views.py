from django.shortcuts import render

# Create your views here.

def createview(request):
    return render(request, 'create.html')


    