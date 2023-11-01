import pandas as pd
from sqlalchemy import text
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus.flowables import PageBreak

# class airports:
#   from_india = "FROM cirium_traffic_asia WHERE \"Orig\" IN ('IXA', 'AMD', 'ATQ', 'BLR', 'BBI', 'MAA', 'CJB', 'DED', 'DEL', 'JWR', 'GOI', 'GOX', 'GAY', 'GAU', 'HYD', 'IMF', 'IDR', 'JAI', 'CNN', 'COK', 'CCU', 'CCJ', 'LKO', 'IXM', 'IXE', 'BOM', 'NAG',  'PNQ', 'IXR', 'IXB', 'SXR', 'STV', 'TRV', 'TIR', 'TRZ', 'BDQ', 'VNS', 'VGA', 'VTZ')"
#   from_usa = ""

# def monthGenerator(year, num):
#     month = ''
#     month2 = ''
#     if (num > 12 & num < 1):
#             return 0
#     if (num >= 10 & num <= 12):
#             month = '-' + str(num) + "-01 00:00:00' "
#             month2 = '-' + str(num) + "-02 00:00:00'"
#     else:
#       month = '-0' + str(num) + "-01 00:00:00' "
#       month2 = '-0' + str(num) + "-02 00:00:00'"
#     return "BETWEEN " + "'" + str(year) + month + 'AND ' + str(year) + month2

# def biannualGenerator(year, num):
#     if (num >= 3 & num <= 0):
#       return 'error'
#     if (num == 1):
#       return "BETWEEN " + "'" + str(year) + "-01-01 00:00:00' " + 'AND ' + str(year) + "-06-02 00:00:00' "
#     else:
#       return "BETWEEN " + "'" + str(year) + "-07-01 00:00:00' " + 'AND ' + str(year) + "-12-02 00:00:00' "

# def qryGenerator(qry, interval, year, num):
#     intv = ''
#     if (interval == 'month'):
#       intv = monthGenerator(year, num)
#     elif (interval == 'biannual'):
#       intv = biannualGenerator(year, num)

#     if (qry == 'total_seats'):
#       qry = qrySwitch.total_seats
#     elif (qry == 'total_pax'):
#       qry = qrySwitch.total_pax
#     return 'SELECT ' + qry + "AND \"Year-Month-Day\" " + intv

# print(qryGenerator('total_seats', 'month','2022', 11))

# locationDict = {"fromUs" : """WHERE "Orig" IN 
#              ('ABE', 'ABI', 'ABR', 'ABY', 'ACK', 'ACT', 'ACV', 'ACY', 'ADK', 'ADQ', 'AEX', 'AGS', 
#              'AKC', 'ALB', 'ALW', 'AMA', 'ANC', 'APN', 'ASE', 'ATL', 'ATW', 'AUG', 'AUS', 'AVL', 
#              'AVP', 'AZO', 'BDL', 'BET', 'BFF', 'BFL', 'BGM', 'BGR', 'BHM', 'BIL', 'BIS', 'BLI', 
#              'BMI', 'BNA', 'BOI', 'BOS', 'BPT', 'BQK', 'BQN', 'BRO', 'BRW', 'BTM', 'BTR', 'BTV', 
#              'BUF', 'BUR', 'BWI', 'BZN', 'CAE', 'CAK', 'CDC', 'CDV', 'CEC', 'CHA', 'CHO', 'CHS', 'CIC', 
#              'CID', 'CKB', 'CLD', 'CLE', 'CLL', 'CLT', 'CMH', 'CMI', 'COD', 'COS', 'CPR', 'CRP', 'CRW', 
#              'CSG', 'CVG', 'CWA', 'DAB', 'DAL', 'DAY', 'DBQ', 'DCA', 'DEN', 'DFW', 'DHN', 'DIK', 'DLG',
#               'DLH', 'DRO', 'DSM', 'DTW', 'DVL', 'EAR', 'EAT', 'EAU', 'ECP', 'EGE', 'EKO', 'ELM', 'ELP', 
#              'ERI', 'EUG', 'EVV', 'EWN', 'EWR', 'EYW', 'FAI', 'FAR', 'FAT', 'FAY', 'FCA', 'FCM', 'FLL', 
#              'FLO', 'FNT', 'FSD', 'FSM', 'FWA', 'FYV', 'GEG', 'GFK', 'GGG', 'GJT', 'GNV', 'GPT', 'GRB', 
#              'GRI', 'GRK', 'GRR', 'GSO', 'GSP', 'GST', 'GTF', 'GTR', 'GUC', 'HNL', 'HOB', 'HOU', 'HPN', 
#              'HRL', 'HSV', 'HTS', 'IAD', 'IAH', 'ICT', 'IDA', 'ILG', 'IND', 'INL', 'ISN', 'ISP', 'ITH', 'ITO', 
#              'IYK', 'JAC', 'JAN', 'JAX', 'JFK', 'JNU', 'KTN', 'LAN', 'LAS', 'LAX', 'LBB', 'LBE', 'LBF', 'LCH', 
#              'LCK', 'LEW', 'LEX', 'LFT', 'LGA', 'LGB', 'LIH', 'LIT', 'LMT', 'LNK', 'LRD', 'LSE', 'LWB', 'LYH',
#               'MBS', 'MCI', 'MCN', 'MCO', 'MDT', 'MDW', 'MEI', 'MEM', 'MFE', 'MFR', 'MHT', 'MIA', 'MKE', 'MKG', 
#              'MLB', 'MLU', 'MOB', 'MOD', 'MOT', 'MQT', 'MVY', 'MYR', 'OAJ', 'OAK', 'OGG', 'OKC', 'OMA', 'ONT', 
#              'ORD', 'ORF', 'OTZ', 'OXR', 'PBI', 'PDX', 'PGD', 'PHL', 'PHX', 'PIE', 'PIR', 'PIT', 'PSC', 'PSG', 'PSP', 
#              'PVD', 'PWM', 'RAP', 'RDD', 'RDM', 'RDU', 'RFD', 'RHI', 'RIC', 'RNO', 'ROC', 'ROW', 'RST', 'RSW', 'SAF', 
#              'SAN', 'SAT', 'SAV', 'SBA', 'SCE', 'SDF', 'SEA', 'SFB', 'SFO', 'SJC', 'SJT', 'SJU', 'SLC', 'SMF', 'SNA', 
#              'SPI', 'SPN', 'SRQ', 'STC', 'STL', 'STT', 'STX', 'SUN', 'SWF', 'SYR', 'TLH', 'TOL', 'TPA', 'TRI', 'TTN', 
#              'TUL', 'TUS', 'TVC', 'TWF', 'TXK', 'TYR', 'TYS', 'UIN', 'USA', 'VLD', 'VPS', 'WRG', 'WYS', 'XNA', 'YAK', 'YUM')
# """}

# selectDict = {"pax" : "SUM(\"Total Pax\")"}

# def traLocGenerator(iatas):
#     iatas = [string.upper() for string in iatas]
#     qrymid = ''
#     qryhead = "WHERE \"Orig\" IN ("
#     qryend = ')'
#     if len(iatas) == 1:
#         qrymid = "'" + iatas[0] + "'"
#     elif len(iatas)>1:
#         for code in iatas:
#             if code != iatas[-1]:
#                 qrymid = qrymid + "'" + code + "'" + ','
#             if code == iatas[-1]:
#                 qrymid = qrymid + "'" + code + "'"
#     return qryhead + " " + qrymid + " " + qryend


# print(traLocGenerator(['Lax', 'syd', 'bne', 'wtf']))

# selectDict = {
#     "AvgYield": """
#     SELECT DATE_TRUNC('month', "Year-Month-Day") as month,
#     AVG("Yield") as yield
#     """
#     ,
#     "SumPax": """
#     SELECT DATE_TRUNC('month', "Year-Month-Day") as month,
#     SUM("Total Pax") as pax
#     """
#     ,
    
# }

# qry = """SELECT
#     DATE_TRUNC('month', \"Year-Month-Day\") as month,
#     AVG(\"Yield\") as yield,
#     SUM(\"Total Pax\") as pax
# FROM cirium_traffic_northamerica
# WHERE
#     \"Orig\" IN ('LAX', 'SFO', 'DFW', 'IAH', 'HNL')
#     AND \"Dest\" IN ('SYD', 'MEL', 'BNE')
# 	AND \"Op Al\" = ('UA')
# 	AND \"Stop-1 Airport\" is null
# 	AND \"Total Pax\" >0
#     AND \"Year-Month-Day\">= '2022-01-01'
# group by
#   month"""

# def qryAssemblr(select, fromschema, where, gorup):
#     return 0

# # Define your PostgreSQL database connection
db_uri = 'postgresql://student003:chihrusvfnihdipp@dataviation-database-1.chl8zbfpbhhh.ap-southeast-2.rds.amazonaws.com/dataviation_tutorial'

# # Create an SQLAlchemy engine
engine = create_engine(db_uri, echo=False)
conn = engine.connect()

def main():
    origin = []
    orig_continent = ''
    destination = []
    while True:
        orig = input("""
                    Enter IATA code of desired origin airports, press enter to enter the next one\n
                    case insensitive, make sure the airports are in the same continent\n
                    type 'q' to finish
        """)
        if orig.lower() == 'q':
            break
        elif len(orig) != 3:
            print('IATA Codes should be 3 letter long')
        orig = orig.upper()
        origin.append(orig)
    
    
    if len(origin) == 0:
        print("need to have at least 1 origin")
        return 0
    
    orig_continent = input(""" enter the continent of the origin airports \n 
                           currently support asia, northamerica, europe, oceania""")

    print("origins:", origin)
    print("orig dest:", orig_continent)

    while True:
        dest = input("""
                    Enter IATA code of desired destination airports, press enter to enter the next one\n
                    case insensitive, currently only supporitng cities in australia \n
                    type 'q' to finish
        """)
        if dest.lower() == 'q':
            break
        elif len(dest) != 3:
            print('IATA Codes should be 3 letter long')
        dest = dest.upper()
        destination.append(dest)

    
    print("destinations", destination)
    final = formatdest(origin, orig_continent, destination)
    tqry = formatfirst(orig_continent, "traffic") + final
    sqry = formatfirst(orig_continent, "schedule") + final
    traffic_df = pd.read_sql_query(text(tqry), conn)
    schedule_df = pd.read_sql_query(text(sqry), conn)

    print("traffic")
    print(traffic_df)
    print("schedule")
    print(schedule_df)

    
    return 0

def formatfirst(continent, tORS):
    options = ['northamerica', 'asia', 'europe', 'oceania']
    tsoptions = ['traffic', 'schedule']
    if continent not in options:
        print('not a valid continent')
        exit(1)
    
    if tORS not in tsoptions:
        print("traffic or schedule")
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
    origstr = '('
    deststr = '('
    
    for source in orig:
        if source != orig[-1]:
            origstr = origstr + "'" + source + "'" + ','
        if source == orig[-1]:
            origstr = origstr + "'" + source + "'"
    origstr = origstr + ')'

    if len(dest) == 0 or dest[0] == '':
        return """
        WHERE "Orig" IN
    """ + origstr + """
    AND "Stop-1 Airport" is null
    """ +"""
    GROUP BY month
    ORDER BY month
    """

    for desti in dest:
        if desti != dest[-1]:
            deststr = deststr + "'" + desti + "'" + ','
        if desti == dest[-1]:
            deststr = deststr + "'" + desti + "'"
    deststr = deststr + ')'

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

if __name__ == "__main__":
    main()