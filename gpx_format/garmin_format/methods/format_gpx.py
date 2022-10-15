import gpxpy
import gpxpy.gpx
import datetime


def remove_waypoints(file):

    # Parse the file and remove all the waypoints
    gpx = gpxpy.parse(file)
    gpx.waypoints = []
    
    return gpx.to_xml()