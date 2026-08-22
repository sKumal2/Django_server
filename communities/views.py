from django.shortcuts import render

# Create your views here.
def communities(request):
    return render(request, 'communities/index.html')


