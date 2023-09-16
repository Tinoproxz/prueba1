from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request,'webappp/index.html')

def electronica(request):
    data= {"titulo": "electronica"}
    return render (request,'webappp/producto.html',data)

def juguete(request):
    data= {"titulo": "juguete"}
    return render (request,'webappp/producto.html',data)

def ropa(request):
    data= {"titulo": "ropa122222"}   
    return render (request,'webappp/producto.html',data)