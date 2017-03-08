#!/usr/bin/env python
#-*- coding: utf-8 -*-
#vim: set fileencoding=utf8:
"""
Get Weather from weather underground
Created 07/03/2017
@author:joanpaucg
"""
import requests
import json
import argparse
api_key=None
class WeatherClient(object):
    """docstring for WeatherClient """
    url_base="https://api.wunderground.com/api/"
    url_service={
    "almanac":"/almanac/q/CA/",
    "hourly":"/hourly/q/CA/",
    "astronomy":"/astronomy/q/CA/",
    "conditions":"/conditions/q/CA/"

    }
    def __init__(self,api_key):
        super(WeatherClient,self).__init__()
        self.api_key=api_key

    def almanac(self,location):
        """
        Accesses wunderground almanac information for the given location
        """
        url=WeatherClient.url_base + self.api_key +\
        WeatherClient.url_service["almanac"] +\
        location + ".json"
        f=requests.get(url)
        return json.loads(f.text)

    def hourly(self,location):
        """
        Accesses wunderground hourly information for the given location
        """
        url=WeatherClient.url_base + self.api_key +\
        WeatherClient.url_service["hourly"] +\
        location + ".json"
        f=requests.get(url)
        return json.loads(f.text)
    def astronomy(self,location):
        """
        Accesses wunderground astronomy information for the given location
        """
        url=WeatherClient.url_base + self.api_key +\
        WeatherClient.url_service["astronomy"] +\
        location + ".json"
        f=requests.get(url)
        return json.loads(f.text)

    def conditions(self,location):
        """
        Accesses wunderground conditions information for the given location
        """
        url=WeatherClient.url_base + self.api_key +\
        WeatherClient.url_service["conditions"] +\
        location + ".json"
        f=requests.get(url)
        return json.loads(f.text)



def print_hourly(hourly):
    """
    Prints an hourly received as a dict
    """
    hourly_forecast=resultat["hourly_forecast"]
    print "Hourly"
    for hour in hourly_forecast:
        print "/**************************************************************/"
        print "Date: %s/%s/%s\nHour: %s:%s" % \
        (hour["FCTTIME"]["mday_padded"],hour["FCTTIME"]["mon_padded"],
         hour["FCTTIME"]["year"],hour["FCTTIME"]["hour_padded"],
         hour["FCTTIME"]["min"])
        print "Weather Forecast:%s\nTemperature:%sC\nhumidity:%s\n" %\
        (hour["wx"],hour["temp"]["metric"],hour["humidity"],)

        print "/**************************************************************/\n"
def print_almanac(almanac):
    """
    Prints an almanac received as a dict
    """
    print "Almanac"
    print "  High Temperatures:"
    print "    Average on this date", almanac['almanac']['temp_high']['normal']['C']
    print "    Record on this date %s (%s) " % \
        (almanac['almanac']['temp_high']['record']['C'],
            almanac['almanac']['temp_high']['recordyear'])
    print "  Low Temperatures:"
    print "    Average on this date", almanac['almanac']['temp_low']['normal']['C']
    print "    Record on this date %s (%s) " % \
        (almanac['almanac']['temp_low']['record']['C'],
         almanac['almanac']['temp_low']['recordyear'])
def print_astronomy(astronomy):
    print "Astronomy"
    print "  Moon phase:"
    print "    Illuminated: "+str(astronomy["moon_phase"]["percentIlluminated"])+" %"
    print "    Age of Moon: "+str(astronomy["moon_phase"]["ageOfMoon"])
    print "    Hemisphere:" + str(astronomy["moon_phase"]["hemisphere"])
    print "    Current Time: %s:%s"%\
    (astronomy["moon_phase"]["current_time"]["hour"],
    astronomy["moon_phase"]["current_time"]["minute"])
    print "    Sun Rise: %s:%s" % (astronomy["moon_phase"]["sunrise"]["hour"]
    ,astronomy["moon_phase"]["sunrise"]["minute"])
    print "    Sunset: %s:%s" % (astronomy["moon_phase"]["sunset"]["hour"],
    astronomy["moon_phase"]["sunset"]["minute"])
    print "    Moon Rise: %s:%s" % (astronomy["moon_phase"]["moonrise"]["hour"],
    astronomy["moon_phase"]["moonrise"]["minute"])
    print "    Moon Set: %s:%s" % (astronomy["moon_phase"]["moonset"]["hour"],
    astronomy["moon_phase"]["moonset"]["minute"])
    print "  Sun Phase"
    print "    Sun Rise: %s:%s" % (astronomy["moon_phase"]["sunrise"]["hour"]
    ,astronomy["sun_phase"]["sunrise"]["minute"])
    print "    Sunset: %s:%s" % (astronomy["moon_phase"]["sunset"]["hour"],
    astronomy["sun_phase"]["sunset"]["minute"])
def print_conditions(conditions):
    print "Conditions"
    print "  Location"
    print "    City: %s"%\
    conditions["current_observation"]["display_location"]["city"]
    print "    Country: %s"%\
    conditions["current_observation"]["display_location"]["state_name"]
    print "    Latitude: %s"%\
    conditions["current_observation"]["display_location"]["latitude"]
    print "    Longitude: %s"%\
    conditions["current_observation"]["display_location"]["longitude"]
    print "    Elevation: %s"%\
    conditions["current_observation"]["display_location"]["elevation"]
    print "  Date\n    %s"%\
    conditions["current_observation"]["local_time_rfc822"]
    print "  Weather"
    print "    weather: %s"%\
    conditions["current_observation"]["weather"]
    print "    Temperature: %s"%\
    conditions["current_observation"]["temperature_string"]
    print "    Humidity: %s"%\
    conditions["current_observation"]["relative_humidity"]
    print "    Wind: %s"%\
    conditions["current_observation"]["wind_string"]




if __name__=='__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                    description="", epilog="")
    parser.add_argument('-al', '--almanac', action='store_true',
                       help="Return High Temperatures and Low Temperatures")
    parser.add_argument('-ho', '--hourly', action='store_true',
                        help="Hourly Forecast")

    parser.add_argument('-as', '--astronomy', action='store_true',
                        help="Return the moon phase,sunrise and sunset times")

    parser.add_argument('-c', '--conditions', action='store_true',
                       help="Return Location, Date and Weahter parameters")
    parser.add_argument('-k', '--key', type=str,
                        help="key to use the api of weather ground")
    opts=parser.parse_args()
    if not api_key:
        try:
            api_key=opts.key
        except IndexError:
            print "API Key must be in CLI option"
    print "-al/almanac:",opts.almanac
    print "-ho/--hourly:", opts.hourly
    print "-as/--astronomy:", opts.astronomy
    print "-c/--conditions:", opts.conditions
    wc=WeatherClient(api_key)
    if opts.hourly:
        resultat=wc.hourly("Lleida")
        print_hourly(resultat)
    if opts.astronomy:
        resultat=wc.astronomy("Lleida")
        print_astronomy(resultat)
    if opts.conditions:
        resultat=wc.conditions("Lleida")
        print_conditions(resultat)
    if opts.almanac:
        resultat=wc.almanac("Lleida")
        print_almanac(resultat)
