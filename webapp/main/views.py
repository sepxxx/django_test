from django.shortcuts import render
# при написании render считаем что уже находимся в папке templates
def index(request):
    return render(request, 'main/index.html')
def about(request):
    return render(request, 'main/about.html')
