import gpxpy
import gpxpy.gpx
import datetime


def remove_waypoints(file):
    gpx = gpxpy.parse(file)
    gpx.waypoints = []
    now = datetime.datetime.now()
    now_str = f"{now.strftime('%d-%m-%yT%H-%M-%S-')}{file.name}"
    file_path = f"gpx/{now_str}"
    with open(f"media/{file_path}", "w+") as tmp:
        tmp.write(gpx.to_xml())
    return file_path