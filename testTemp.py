import urllib2
import json
from flask import request
from flask import Flask

app = Flask(__name__)


@app.route('/query')
def hello():
    key = 'eb33c6e223981272af58a0b76ff1901b'
    url = 'http://api.openweathermap.org/data/2.5/weather?q='
    value = request.args.to_dict()  #creating dictionary from query data

    tempList = [] # empty temp list
    cityList = value.values()  #creating list from all cities
    for item in cityList:
        city = str(item)  #cating from list to string to be able to request url
        final_url = url + city + '&appid=' + key
        data_obj = urllib2.urlopen(final_url)
        data = json.load(data_obj)
        tempF = data['main']['temp']
        tempC = int(tempF - 273.15)  #calulating from pharingate to c
        tempList.append(tempC) #creating list with temps
    finalDict = dict(zip(cityList,tempList))

    # printing out data
    return '<h2><center>Temperature in citys you have choosen is   %s </center></h2>' %finalDict


if __name__ == '__main__':
    app.run()
