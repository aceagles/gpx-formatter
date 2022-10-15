from django.shortcuts import render
from .methods.format_gpx import remove_waypoints
from django.http import HttpResponse
from .models import GPXFile

# Create your views here.
def file_upload_view(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        new_entry = GPXFile()
        new_entry.newfile.name = remove_waypoints(myfile)
        new_entry.save()
        xml_gpx = myfile.read()
        return HttpResponse("<textarea>"+str(xml_gpx)+"</textarea>")
    return render(request, "upload/upload_form.html", {})