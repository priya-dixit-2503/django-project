from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data={
        'title':'New Home Page',
        'bdata': 'welcome to wscubetech',
        'clist':['PHP','java','django'],
        'student_details' :[
            {'name':'priya','phoneNo':3333333322},
            {'name':'priyanka','phoneNo':33223333322},
        ]
    }
    return render(request,"index.html",data)


def course(request):
    return HttpResponse("welcome to wscubetech course")

def courseDetails(request,courseId):
    return HttpResponse(courseId)   
    
