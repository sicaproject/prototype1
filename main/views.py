from django.shortcuts import render
from django.views import View

# Create your views here.

class start2(View):
    def get(self,request):
        return render(request,'main/index.html')