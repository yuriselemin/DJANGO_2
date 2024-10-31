from django.shortcuts import render



def func_render(request):
    return render(request, 'second_task/func_template.html')