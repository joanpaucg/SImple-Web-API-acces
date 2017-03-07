#/usr/bin/env python
#-*- coding: utf-8 -*-
#vim: set fileencoding=utf8:
"""
Get Weather from weather underground
Created 07/03/2017
@author:joanpaucg
"""
import sys
import requests
import json
api_key=None
class WeatherClient(object):
    """docstring for WeatherClient """
    url_base="https://api.wunderground.com/api/"
    url_service={
    "hourly":"/hourly/q/CA/"

    }
    def __init__(self,api_key):
        super(WeatherClient,self).__init__()
        self.api_key=api_key
    def hourly(self,location):
        #baixar-se la pagina web
        url=WeatherClient.url_base + self.api_key +\
        WeatherClient.url_service["hourly"] +\
        location + ".json"
        f=requests.get(url)
        return json.loads(f.text)

def print_hourly(hourly):
    hourly_forecast=resultat["hourly_forecast"]
    for hour in hourly_forecast:
        print "/**************************************************************/"
        print "Date: %s/%s/%s\nHour: %s:%s" % \
        (hour["FCTTIME"]["mday_padded"],hour["FCTTIME"]["mon_padded"],
         hour["FCTTIME"]["year"],hour["FCTTIME"]["hour_padded"],
         hour["FCTTIME"]["min"])
        print "Weather Forecast:%s\nTemperature:%sC\nhumidity:%s\n" %\
        (hour["wx"],hour["temp"]["metric"],hour["humidity"],)

        print "/**************************************************************/\n"



if __name__=='__main__':
    if not api_key:
        try:
            api_key=sys.argv[1]
        except IndexError:
            print "API Key must be in CLI option"
    wc=WeatherClient(api_key)
    resultat=wc.hourly("Lleida")
    print_hourly(resultat)

    #print resultat
