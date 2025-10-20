from django.http import HttpResponse
from django.http import HttpResponse

# Create your views here.
def students(request):
    return HttpResponse("Hello, this is the students view!")