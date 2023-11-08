import pandas as pd
from sqlalchemy import text
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select
from qry_generation_trsch import formatAirports

# # Define your PostgreSQL database connection
db_uri = 'postgresql://student003:chihrusvfnihdipp@dataviation-database-1.chl8zbfpbhhh.ap-southeast-2.rds.amazonaws.com/dataviation_tutorial'

# # Create an SQLAlchemy engine
engine = create_engine(db_uri, echo=False)
conn = engine.connect()

def generateAl(origin, orig_continent, destination):
    
    final = getairline1(orig_continent) + getairline2(origin, destination)
    topal_df = pd.read_sql_query(text(final), conn)
    
    variables = topal_df['airline'].tolist()
    airline_df = pd.DataFrame()
    for vara in variables:
        qry = getseats1(orig_continent) + getseats2(origin, destination,vara)
        temp_df = pd.read_sql_query(text(qry), conn)
        airline_df = pd.concat([airline_df, temp_df])

    al_df = topal_df.merge(airline_df, on = 'airline', how = 'inner')
    print(al_df)
    return topal_df

def getseats1(continent):
    firstStr = """
    SELECT "Op Al" as airline, SUM("Seats") as seats
    """ + "FROM cirium_schedule_"+continent
    return firstStr

    

def getairline1(continent):
    firstStr = """
    SELECT "Op Al" as airline, SUM("Total Pax") AS total_pax
    """ + "FROM cirium_traffic_"+continent

    return firstStr

def getseats2(orig, dest, airline):
    origstr = formatAirports(orig)
    finalstr = formatAirports(dest)
    
    if len(dest) == 0 or dest[0]=='':
        return """
        WHERE "Orig" IN
        """ + origstr + """
        AND "Stop-1 Airport" is null
        """ + """AND "Op Al" IN ('""" + airline + "') Group by airline"
    
    final = """
        WHERE "Orig" IN
    """ + origstr + """
    AND "Dest" IN
    """ + finalstr + """
    AND "Stop-1 Airport" is null
    """ + """AND "Op Al" IN ('""" + airline + "') Group by airline"

    return final
 

def getairline2(orig, dest):
    finalstr = """
    Group by airline
    Order by total_pax DESC
    limit 4;
    """
    origstr = formatAirports(orig)
    deststr = formatAirports(dest)
    if len(dest) == 0 or dest[0]=='':
        return """
        WHERE "Orig" IN
        """ + origstr + """
        AND "Stop-1 Airport" is null
        """ + finalstr
    
    final = """
        WHERE "Orig" IN
    """ + origstr + """
    AND "Dest" IN
    """ + deststr + """
    AND "Stop-1 Airport" is null
    """ + finalstr

    return final
    
# SELECT "Op Al" as airline, SUM("Total Pax") AS total_pax
# FROM cirium_traffic_asia
# Group by airline
# Order by total_pax DESC
# limit 3;
