from django.shortcuts import render

# Create your views here.
def new(request):
    d={'name':'SEENU','mno':'90909090','age':'18+'}
    return render(request,'new.html',context=d)