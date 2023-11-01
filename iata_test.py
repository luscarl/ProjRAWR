import airportsdata
airports = airportsdata.load()
lab = 0
for a in airports:
    icao, iata, name, city, subd, country, elevation, lat, lon, tz, lid = airports[a]
    if country != 'US':
        print(airports[a])
