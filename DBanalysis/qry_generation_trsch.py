import pandas as pd
from sqlalchemy import text
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select

# # Define your PostgreSQL database connection
db_uri = 'postgresql://student003:chihrusvfnihdipp@dataviation-database-1.chl8zbfpbhhh.ap-southeast-2.rds.amazonaws.com/dataviation_tutorial'

# # Create an SQLAlchemy engine
engine = create_engine(db_uri, echo=False)
conn = engine.connect()

def generateTRSC(origin, orig_continent, destination):
    final = formatdest(origin, orig_continent, destination)
    tqry = formatfirst(orig_continent, 'traffic') + final
    sqry = formatfirst(orig_continent, 'schedule') + final
    traffic_df = pd.read_sql_query(text(tqry), conn)
    schedule_df = pd.read_sql_query(text(sqry), conn)
    trsch_df = traffic_df.merge(schedule_df, on = 'month', how = 'inner')
def formatAirports(aps):
    finalstrst = '('
    for source in aps:
        if source != aps[-1]:
            finalstrst = finalstrst + "'" + source + "'" + ','
        if source == aps[-1]:
            finalstrst = finalstrst + "'" + source + "'"
    finalstrst = finalstrst + ')'
    return finalstrst

def formatfirst(continent, tORS):
    options = ['northamerica', 'asia', 'europe', 'oceania']
    tsoptions = ['traffic', 'schedule']
    if continent not in options:
        print('not a valid continent')
        exit(1)
    
    if tORS not in tsoptions:
        print("has to be traffic or schedule")
        exit(1)

    if tORS == 'traffic':
        qrystart = """
        SELECT DATE_TRUNC('month', \"Year-Month-Day\") as month,
        AVG("Yield") as yield, SUM("Total Pax") as pax, 
        AVG("% POO Orig") as porig, AVG("Rev") as rev 
        """ + "FROM cirium_traffic_" + continent 
    
    if tORS == 'schedule':
        qrystart = """
        SELECT DATE_TRUNC('month', \"Year-Month-Day\") as month,
        SUM("Seats") as seats, AVG("ASKs") as ask 
        """ + "FROM cirium_schedule_" +continent 
    
    return qrystart


def formatdest(orig, continent, dest):
    origstr = formatAirports(orig)
    deststr = formatAirports(dest)
    if len(dest) == 0 or dest[0] == '':
        return """
        WHERE "Orig" IN
    """ + origstr + """
    AND "Stop-1 Airport" is null
    """ +"""
    GROUP BY month
    ORDER BY month
    """

    finalstr = """
        WHERE "Orig" IN
    """ + origstr + "AND" + """
        "Dest" IN
    """ + deststr + """
    AND "Stop-1 Airport" is null
    """ +"""
    GROUP BY month
    ORDER BY month
    """

    return finalstr
