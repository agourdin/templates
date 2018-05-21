from django.shortcuts import render

def mockup(request):
    return render(request, 'index.html')
