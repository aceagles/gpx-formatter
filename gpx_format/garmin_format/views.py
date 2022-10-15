from django.shortcuts import render
from .methods.format_gpx import remove_waypoints
from django.http import HttpResponse
from .models import GPXFile
import datetime

def file_upload_view(request):
    file = None
    
    # View self references so if a file is present then process and output
    if request.method == 'POST' and request.FILES['myfile']:

        myfile = request.FILES['myfile']

        # Create a new entry in the GPX table
        new_entry = GPXFile()

        #format the gpx
        new_gpx = remove_waypoints(myfile)

        # Create a file with the new gpx
        now = datetime.datetime.now()
        now_str = f"{now.strftime('%d-%m-%yT%H-%M-%S-')}{myfile.name}"
        file_path = f"gpx/{now_str}"
        with open(f"media/{file_path}", "w+") as tmp:
            tmp.write(new_gpx)
        
        # Add the new file to the table
        new_entry.newfile.name = file_path
        new_entry.save()

        # Set the file variable to be returned to the template
        file = new_entry
    return render(request, "upload/upload_form.html", {'file': file})