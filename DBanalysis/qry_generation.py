import pandas as pd
from qry_generation_trsch import *
from qry_generation_al import *
from pdf_generation import *
from qry_generation_route import *

def getInfo():
    origin = []
    orig_continent = ''
    destination = []
    while True:
        orig = input("""
                    Enter IATA code of desired origin airports, press enter to enter the next one\n
                    case insensitive, make sure the airports are in the same continent\n
                    type 'q' to finish: 
        """)
        if orig.lower() == 'q':
            break
        elif len(orig) != 3:
            print('IATA Codes should be 3 letter long')
            continue
        orig = orig.upper()
        origin.append(orig)
    
    if len(origin) == 0:
        print("need to have at least 1 origin")
        exit(0)
    
    orig_continent = input(""" enter the continent of the origin airports \n 
                           currently support asia, northamerica, europe, oceania: """)

    while True:
        dest = input("""
                    Enter IATA code of desired destination airports, press enter to enter the next one\n
                    case insensitive, currently only supporitng cities in australia \n
                    type 'q' to finish: 
        """)
        if dest.lower() == 'q':
            break
        elif len(dest) != 3:
            print('IATA Codes should be 3 letter long')
        dest = dest.upper()
        destination.append(dest)

    trsch_df = generateTRSC(origin, orig_continent, destination)
    al_df = generateAl(origin, orig_continent, destination)
    topr_df = generateR(origin, orig_continent, destination)
    formatPDF(trsch_df, al_df, topr_df,origin, destination)


if __name__ == "__main__":
    getInfo()
