from django.shortcuts import render,redirect,HttpResponse
from .models import GameInfo
# Create your views here.
def index(request):
    return render(request,'pages/index.html')
def gameInfo(request):
        if request.method=='POST':
                temp_id = request.POST["temp_id"]
                first_name = request.POST["first_name"]
                last_name = request.POST["last_name"]
                gender = request.POST["gender"]
                ranking = -1
                age = request.POST["age"]
                singles = 'singles' in request.POST
                doubles = 'doubles' in request.POST
                mix_double = 'mix_double' in request.POST
                all_mix_double ='all_mix_double' in request.POST
                gameInfo = GameInfo(first_name=first_name,last_name=last_name,gender=gender,ranking=ranking,age=age,singles=singles,doubles=doubles,mix_double=mix_double,all_mix_double=all_mix_double,temp_id=temp_id)
                gameInfo.save()
                return HttpResponse("Success")
        return HttpResponse("Success")
