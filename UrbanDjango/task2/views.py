from django.shortcuts import render

def render_class(request):
    return render(request, 'class_template.html')

def func_class(request):
    return render(request, 'func_template.html')