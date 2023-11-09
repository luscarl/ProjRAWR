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
    print(f"Producing top airlines in terms of {formatAirports(origin)} to {formatAirports(destination)}")
    variables = topal_df['airline'].tolist()
    print(topal_df)
    for vara in variables:
        print(destination)
        print(generateAlMonth(vara, orig_continent, origin, destination))
    return topal_df

def generateAlMonth(airline, continent, orig, dest):

    if len(dest) == 0 or dest[0] == '':
        return f"""SELECT DISTINCT ON (DATE_TRUNC('month',"Year-Month-Day")) DATE_TRUNC('month', "Year-Month-Day")as month, 
                sum("Total Pax") as {airline} 
                FROM cirium_traffic_{continent}
                WHERE "Year-Month-Day" >= '2022-01-01'
                AND "Orig" IN {formatAirports(orig)}
                AND "Op Al" IN ('{airline}')
                group by "Year-Month-Day"
                """
    
    return f"""SELECT DISTINCT ON (DATE_TRUNC('month',"Year-Month-Day")) DATE_TRUNC('month', "Year-Month-Day")as month, 
                sum("Total Pax") as {airline} 
                FROM cirium_traffic_{continent}
                WHERE "Year-Month-Day" >= '2022-01-01'
                AND "Orig" IN {formatAirports(orig)}
                AND "Dest" IN {formatAirports(dest)}
                AND "Op Al" IN ('{airline}')
                group by "Year-Month-Day"
                """

def getairline1(continent):
    firstStr = """
    SELECT "Op Al" as airline, SUM("Total Pax") AS total_pax
    """ + "FROM cirium_traffic_"+continent

    return firstStr
 

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
