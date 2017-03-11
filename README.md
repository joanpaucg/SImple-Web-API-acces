# SImple-Web-API-acces
Exercici opcional de l'assignatura Sistemes i Tecnologies Web

This program gives you a few almanac,hourly,astronomy,conditions values from 
https://www.wunderground.com/weather/api/d/docs?d=data/

To run the program, you need to have an apy key and you have to put on command line:

python simpleweb.py [-h] -k KEY [-al] [-ho] [-as] [-c]

You have to choose optional options to print results.

optional arguments:
  -h, --help         show this help message and exit
  -k KEY, --key KEY  key to use the api of weather ground (default: None)
  -al, --almanac     Return High Temperatures and Low Temperatures (default:
                     False)
  -ho, --hourly      Hourly Forecast (default: False)
  -as, --astronomy   Return the moon phase,sunrise and sunset times (default:
                     False)
  -c, --conditions   Return Location, Date and Weahter parameters (default:
                     False)

