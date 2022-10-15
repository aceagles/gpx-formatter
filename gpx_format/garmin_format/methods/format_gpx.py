import gpxpy
import gpxpy.gpx
import datetime


def remove_waypoints(file):
    gpx = gpxpy.parse(file)
    gpx.waypoints = []
    now = datetime.datetime.now()
    now_str = now.strftime("%d-%m-%y-%H-%M-%S.gpx")
    with open("media/gpx/"+now_str, "w+") as tmp:
        tmp.write(gpx.to_xml())
    return gpx.to_xml()