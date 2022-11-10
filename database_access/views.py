from django.shortcuts import render
from django.http import HttpResponse
import database_access
 
# Create your views here.
def index(request):
    url = request.GET.get('url')
    return HttpResponse(database_access.gettext(url), content_type = 'application/json')

