from django.shortcuts import render

# Create your views here.
def c_index(request):
    return render(request,'c/index.html')
