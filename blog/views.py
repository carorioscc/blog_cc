from django.shortcuts import render

# Create your views here.
#AQUI SE COLOCAN LAS VISTAS
def post_list(request):
    return render(request, 'blog/post_list.html', {})