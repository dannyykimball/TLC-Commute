def GetGeojson(toplace, fromplace, date, time, outputfile):
    url = 'http://localhost:8080/otp/routers/current/isochrone'
    param = { 'toPlace': toplace,
              'fromPlace': fromplace,
              'arriveBy': True,
              'mode': 'WALK,TRANSIT',
              'date': date,
              'time': time,
              'maxWalkDistance':1600,
              'walkReluctance': 5,
              'minTransferTime': 600,
              'cutoffsec': 900,
              'cutoffsec': 1800,
              'cutoffsec': 2700,
              'cutoffsec': 3600,
              'cutoffsec': 4500,
              'cutoffsec': 5400
              }
    response = requests.get(url,params = param)
    with open (outputfile, 'w') as f:
        geojson.dump(response,f)