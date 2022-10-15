from django.shortcuts import render
from .methods.format_gpx import remove_waypoints
from django.http import HttpResponse
from .models import GPXFile

# Create your views here.
def file_upload_view(request):
    file = None
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        new_entry = GPXFile()
        new_entry.newfile.name = remove_waypoints(myfile)
        new_entry.save()
        file = new_entry
    return render(request, "upload/upload_form.html", {'file': file})