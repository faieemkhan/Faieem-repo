from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable':"this",
    }
    return render(request,'index.html',context)
    #return HttpResponse("this is home page")
def courses(request):
    return render(request,'courses.html')
def youtube(request):
    return render(request,'index.html')
def privacy(request):
    return render(request,'privacy.html')
def about(request):
    return render(request,'about.html')
