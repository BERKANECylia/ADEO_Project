from django.shortcuts import render
from .models import PRG_STUDENT_SITE
from django.http import HttpResponse

#@login_required(login_url='/login')
def PRG_STUDENT_SITE_View(request,*args,**kwargs):
   query_results=PRG_STUDENT_SITE.objects.all()
   context={'query_results':query_results}
   #return render(request,'',context)
   #return render(request,"PRGSTUDENTSITE.html",{})
   return render(request,"PRGSTUDENTSITE.html",context)



#def PRG_STUDENT_SITE_View(*args,**kwargs):
#    return HttpResponse('<h1>Display PRG_STUDENT_SITE_view</h1>')

# Create your views here.

