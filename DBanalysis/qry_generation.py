import pandas as pd
from sqlalchemy import text
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select
from qry_generation_trsch import *
from qry_generation_al import *

# # Define your PostgreSQL database connection
db_uri = 'postgresql://student003:chihrusvfnihdipp@dataviation-database-1.chl8zbfpbhhh.ap-southeast-2.rds.amazonaws.com/dataviation_tutorial'

# # Create an SQLAlchemy engine
engine = create_engine(db_uri, echo=False)
conn = engine.connect()

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

    generateTRSC(origin, orig_continent, destination)
    generateAl(origin, orig_continent, destination)

    # final = formatdest(origin, orig_continent, destination)
    # tqry = formatfirst(orig_continent, "traffic") + final
    # sqry = formatfirst(orig_continent, "schedule") + final
    # traffic_df = pd.read_sql_query(text(tqry), conn)
    # schedule_df = pd.read_sql_query(text(sqry), conn)

    # trsch_df = traffic_df.merge(schedule_df, on = 'month', how = 'inner')
    # print(trsch_df)
    # return trsch_df


if __name__ == "__main__":
    getInfo()
