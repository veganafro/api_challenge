import urllib2
import json

token = "7629edd01fdbb13225e5ffed34449294"
github
end_point = "http://challenge.code2040.org/api/register"

json_obj = urllib2.urlopen(end_point)

json.load(json_obj)