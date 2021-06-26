import json
import start
from flask import Flask
from flask import request

app = Flask(__name__)

# returns json of names + coordinats


@app.route('/list')
def getList():
    list = {'jumpPoints': []}
    for i in sites:
        pom = sites.get(i)
        list.get('jumpPoints').append(
            {i: {'lon': pom.get('lon'), 'lan': pom.get('lan')}})
    return json.dumps(list)

# returns json of data for given name + coordinats


@app.route('/data', methods=['GET', 'POST'])
def getData():
    name = request.args["name"]
    atributes = sites.get(name)
    x = atributes.get('lon')
    y = atributes.get('lat')
    ok = atributes.get('ok')
    t = start(name, x, y, ok)
    jumpPoint = {
        "WindSpeed": t.getWindSpeed,  # double
        "WindBust": t.getWindBust(),  # double
        "WindDirection": t.getWindDirection(),  # chat or str
        "Temperature": t.getTemperature(),  # double
        "TimeAndDate": t.getTimeAndDate(),  # date
        "isWindGood": t.isWindGood()  # T/F
    }
    return json.dumps(jumpPoint)


# run() - runs the application on the local development server.
#app.run([host, port, debug, options])
# host - Hostname to listen on. Defaults to 127.0.0.1 (localhost).
# port - defaults to 5000
if __name__ == '__main__':
    app.run()


# hardcoded list of sites, could get list from scraping
sites = {
    'Gozd': {
        'lon': 46.3395,
        'lan': 14.3313,
        'ok': {'JZ', 'J', 'JV'}
    },
    'Ratitovec': {
        'lon': 46.2361,
        'lan': 14.0906,
        'ok': {'J', 'JV'}
    },
    'Vogar': {
        'lon': 46.2946,
        'lan': 13.8755,
        'ok': {'JZ', 'J', 'JV'}
    },
    'Vogel': {
        'lon': 46.2518,
        'lan': 13.839,
        'ok': {'JV', 'V', 'SV'}
    },
    'Kranjska Gora': {
        'lon': 46.5044,
        'lan': 13.7954,
        'ok': {'J'}
    },
    'Ambrož pod Krvavcem': {
        'lon': 46.2752,
        'lan': 14.5279,
        'ok': {'JZ', 'J', 'JV'}
    },
    'Kriška gora': {
        'lon': 46.3515,
        'lan': 14.3332,
        'ok': {'JZ', 'J', 'JV'}
    },
    'Velika planina': {
        'lon': 46.2946,
        'lan': 14.6395,
        'ok': {'J', 'JV'}
    },
    'Mangrtsko Sedlo': {
        'lon': 46.4334,
        'lan': 13.6407,
        'ok': {'JZ', 'J', 'JV', 'V', 'Z'}
    },
    'Kobala': {
        'lon': 46.1806,
        'lan': 13.7791,
        'ok': {'JZ', 'J', 'JV', 'V', 'Z'}
    },
    'Kovk': {
        'lon': 45.8865,
        'lan': 13.9591,
        'ok': {'JZ', 'J', 'JV'}
    },
    'Kobariški Stol': {
        'lon': 46.2727,
        'lan': 13.4732,
        'ok': {'JZ', 'J', 'JV', 'V', 'Z'}
    },
    'Srednji vrh - Matajur': {
        'lon': 46.209,
        'lan': 13.5663,
        'ok': {'SV', 'S'}
    },
    'Kobariški Kuk - jug': {
        'lon': 46.1952,
        'lan': 13.6198,
        'ok': {'JZ', 'J', 'JV'}
    },
    'Lijak': {
        'lon': 45.9636,
        'lan': 13.7236,
        'ok': {'JZ', 'J', 'JV', 'V', 'Z'}
    },
    'Slivnica': {
        'lon': 45.7886,
        'lan': 14.4067,
        'ok': {'JZ', 'J', 'JV', 'Z'}
    },
    'Slivnica': {
        'lon': 45.7886,
        'lan': 14.4067,
        'ok': {'JZ', 'J', 'JV', 'Z'}
    },
    'Kamšak': {
        'lon': 46.3579,
        'lan': 15.259,
        'ok': {'JZ', 'J'}
    },
    'Konjiška gora': {
        'lon': 46.3347,
        'lan': 15.3466,
        'ok': {'JZ', 'J'}
    },
    'Mala Gora': {
        'lon': 46.3574,
        'lan': 15.3397,
        'ok': {'JZ', 'V', 'SV'}
    },
    'Malič': {
        'lon': 46.1822,
        'lan': 15.2056,
        'ok': {'J', 'JV'}
    },
    'Donačka gora': {
        'lon': 46.2616,
        'lan': 15.7313,
        'ok': {'JZ', 'J', 'JV'}
    },
    'Žusem': {
        'lon': 46.1519,
        'lan': 15.4909,
        'ok': {'V', 'SV', 'S'}
    },
    'Pohorje': {
        'lon': 46.5164,
        'lan': 15.58,
        'ok': {'SV', 'S', 'SZ'}
    },
    'Golte': {
        'lon': 46.3705,
        'lan': 14.9206,
        'ok': {'J', 'JV', 'V'}
    },
    'Golte': {
        'lon': 46.3705,
        'lan': 14.9206,
        'ok': {'J', 'JV', 'V'}
    }
}
