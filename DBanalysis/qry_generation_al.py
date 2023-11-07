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
    final = ''
    finalformat = formatTopAlst(orig_continent)
    print(final)

def formatTopAlst(continent):
    firstStr = """
    SELECT "Op Al" as airline, SUM("Total PAX") AS total_pax
    """ + "FROM cirium_traffic_"+continent

def formatTopAlend(orig, dest):
    finalstr = """
    Group by airline
    Order by total_pax DESC
    limit 4;
    """
    origstr = formatAirports(orig)
    deststr = formatAirports(dest)
    if len(dest) == 0 or dest[0]=='':



    return finalstr
    
# SELECT "Op Al" as airline, SUM("Total Pax") AS total_pax
# FROM cirium_traffic_asia
# Group by airline
# Order by total_pax DESC
# limit 3;
