from django.shortcuts import render

# Create your views here.
def home(request):
    user = [{'name' : 'Samir'},
            {'name' : 'Sagun'}]
    return render(request, 'home/index.html', {
        'active_user' : True,
        'user' : user
    })
