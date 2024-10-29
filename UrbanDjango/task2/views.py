from django.shortcuts import render

def render_class(request):
    return render(request, 'class_template.html')

def render_func(request):
    return render(request, 'func_template.html')