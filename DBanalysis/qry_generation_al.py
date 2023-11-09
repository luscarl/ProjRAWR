import pandas as pd
from sqlalchemy import create_engine, text
from qry_generation_trsch import formatAirports

# PostgreSQL database connection
db_uri = 'postgresql://student003:chihrusvfnihdipp@dataviation-database-1.chl8zbfpbhhh.ap-southeast-2.rds.amazonaws.com/dataviation_tutorial'

# SQLAlchemy engine
engine = create_engine(db_uri, echo=False)
conn = engine.connect()

def generateAl(origin, orig_continent, destination):
    final = getairline1(orig_continent) + getairline2(origin, destination)
    topal_df = pd.read_sql_query(text(final), conn)
    print(f"Producing top airlines in terms of {formatAirports(origin)} to {formatAirports(destination)}")
    variables = topal_df['airline'].tolist()
    print("Determined top airlines flying this route, proceding to fetch airline data ..")
    talpax_df = pd.DataFrame()
    taly_df = pd.DataFrame()
    talr_df = pd.DataFrame()
    for vara in variables:
        alqry = generateAlMonthpax(vara, orig_continent, origin, destination)
        t_df = pd.read_sql_query(text(alqry), conn)
        if talpax_df.empty:
            talpax_df = t_df
        else:
            talpax_df = talpax_df.merge(t_df, on = 'month', how = 'inner')
    
    for vara in variables:
        alqry = generateAlMonthy(vara, orig_continent, origin, destination)
        t_df = pd.read_sql_query(text(alqry), conn)
        if taly_df.empty:
            taly_df = t_df
        else:
            taly_df = taly_df.merge(t_df, on = 'month', how = 'inner')

    for vara in variables:
        alqry = generateAlMonthr(vara, orig_continent, origin, destination)
        t_df = pd.read_sql_query(text(alqry), conn)
        if talr_df.empty:
            talr_df = t_df
        else:
            talr_df = talr_df.merge(t_df, on = 'month', how = 'inner')

    return (topal_df, talpax_df, taly_df, talr_df)

def generateAlMonthy(airline, continent, orig, dest):
    if len(dest) == 0 or dest[0] == '':
        return f"""SELECT DISTINCT ON (DATE_TRUNC('month',"Year-Month-Day")) DATE_TRUNC('month', "Year-Month-Day")as month, 
                avg("Yield") as {airline} 
                FROM cirium_traffic_{continent}
                WHERE "Year-Month-Day" >= '2022-01-01'
                AND "Orig" IN {formatAirports(orig)}
                AND "Op Al" IN ('{airline}')
                AND "Stop-1 Airport" IS NULL
                group by "Year-Month-Day"
                """
    
    return f"""SELECT DISTINCT ON (DATE_TRUNC('month',"Year-Month-Day")) DATE_TRUNC('month', "Year-Month-Day")as month, 
                avg("Yield") as {airline} 
                FROM cirium_traffic_{continent}
                WHERE "Year-Month-Day" >= '2022-01-01'
                AND "Orig" IN {formatAirports(orig)}
                AND "Dest" IN {formatAirports(dest)}
                AND "Op Al" IN ('{airline}')
                AND "Stop-1 Airport" IS NULL
                group by "Year-Month-Day"
                """

def generateAlMonthr(airline, continent, orig, dest):
    if len(dest) == 0 or dest[0] == '':
        return f"""SELECT DISTINCT ON (DATE_TRUNC('month',"Year-Month-Day")) DATE_TRUNC('month', "Year-Month-Day")as month, 
                avg("Rev") as {airline} 
                FROM cirium_traffic_{continent}
                WHERE "Year-Month-Day" >= '2022-01-01'
                AND "Orig" IN {formatAirports(orig)}
                AND "Op Al" IN ('{airline}')
                AND "Stop-1 Airport" IS NULL
                group by "Year-Month-Day"
                """
    
    return f"""SELECT DISTINCT ON (DATE_TRUNC('month',"Year-Month-Day")) DATE_TRUNC('month', "Year-Month-Day")as month, 
                avg("Rev") as {airline} 
                FROM cirium_traffic_{continent}
                WHERE "Year-Month-Day" >= '2022-01-01'
                AND "Orig" IN {formatAirports(orig)}
                AND "Dest" IN {formatAirports(dest)}
                AND "Op Al" IN ('{airline}')
                AND "Stop-1 Airport" IS NULL
                group by "Year-Month-Day"
                """

def generateAlMonthpax(airline, continent, orig, dest):
    if len(dest) == 0 or dest[0] == '':
        return f"""SELECT DISTINCT ON (DATE_TRUNC('month',"Year-Month-Day")) DATE_TRUNC('month', "Year-Month-Day")as month, 
                sum("Total Pax") as {airline} 
                FROM cirium_traffic_{continent}
                WHERE "Year-Month-Day" >= '2022-01-01'
                AND "Orig" IN {formatAirports(orig)}
                AND "Op Al" IN ('{airline}')
                AND "Stop-1 Airport" IS NULL
                group by "Year-Month-Day"
                """
    
    return f"""SELECT DISTINCT ON (DATE_TRUNC('month',"Year-Month-Day")) DATE_TRUNC('month', "Year-Month-Day")as month, 
                sum("Total Pax") as {airline} 
                FROM cirium_traffic_{continent}
                WHERE "Year-Month-Day" >= '2022-01-01'
                AND "Orig" IN {formatAirports(orig)}
                AND "Dest" IN {formatAirports(dest)}
                AND "Op Al" IN ('{airline}')
                AND "Stop-1 Airport" IS NULL
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
