from django.shortcuts import render
from .methods.format_gpx import remove_waypoints
from django.http import HttpResponse

# Create your views here.
def file_upload_view(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        xml_gpx = remove_waypoints(myfile)
        return HttpResponse("<textarea>"+str(xml_gpx)+"</textarea>")
    return render(request, "upload/upload_form.html", {})