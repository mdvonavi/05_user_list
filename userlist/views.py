from django.shortcuts import render
from . models import UserList
from django.http import HttpResponse

def userlist(request):
    data = {
            'users': UserList.objects.all()
        }
    if request.method == "POST":
        print(request.POST.get('fname_input'))
        new_user = UserList(fname = request.POST.get('fname_input'), lname = request.POST.get('lname_input'), email = request.POST.get('email_input'), age = request.POST.get('age_input'), city = request.POST.get('city_input'))
        new_user.save()
        return render(request, 'userlist/index.html', data)
    else:
        return render(request, 'userlist/index.html', data)
