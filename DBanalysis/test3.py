import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy import MetaData
import matplotlib.pyplot as plt
from matplotlib import ticker

# # Define your PostgreSQL database connection
db_uri = 'postgresql://student003:chihrusvfnihdipp@dataviation-database-1.chl8zbfpbhhh.ap-southeast-2.rds.amazonaws.com/dataviation_tutorial'

# # Create an SQLAlchemy engine
engine = create_engine(db_uri, echo=False)
conn = engine.connect()

class qrySwitch:
  total_seats = " SUM(\"Seats\") "
  total_pax = " SUM(\"Total pax\") "
  total_rev = " SUM(\"Rev\") "

class airports:
  from_india = "FROM cirium_traffic_asia WHERE \"Orig\" IN ('IXA', 'AMD', 'ATQ', 'BLR', 'BBI', 'MAA', 'CJB', 'DED', 'DEL', 'JWR', 'GOI', 'GOX', 'GAY', 'GAU', 'HYD', 'IMF', 'IDR', 'JAI', 'CNN', 'COK', 'CCU', 'CCJ', 'LKO', 'IXM', 'IXE', 'BOM', 'NAG',  'PNQ', 'IXR', 'IXB', 'SXR', 'STV', 'TRV', 'TIR', 'TRZ', 'BDQ', 'VNS', 'VGA', 'VTZ')"

def monthGenerator(year, num):
    month = ''
    month2 = ''
    if (num > 12 & num < 1):
            return 0
    if (num >= 10 & num <= 12):
            month = '-' + str(num) + "-01 00:00:00' "
            month2 = '-' + str(num) + "-02 00:00:00'"
    else:
      month = '-0' + str(num) + "-01 00:00:00' "
      month2 = '-0' + str(num) + "-02 00:00:00'"
    return "BETWEEN " + "'" + str(year) + month + 'AND ' + str(year) + month2

def biannualGenerator(year, num):
    if (num >= 3 & num <= 0):
      return 'error'
    if (num == 1):
      return "BETWEEN " + "'" + str(year) + "-01-01 00:00:00' " + 'AND ' + str(year) + "-06-02 00:00:00' "
    else:
      return "BETWEEN " + "'" + str(year) + "-07-01 00:00:00' " + 'AND ' + str(year) + "-12-02 00:00:00' "

def qryGenerator(qry, interval, year, num):
    intv = ''
    qry = ''
    if (interval == 'month'):
      intv = monthGenerator(year, num)
    elif (interval == 'biannual'):
      intv = biannualGenerator(year, num)

    if (qry == 'total_seats'):
      qry = qrySwitch.total_seats
    elif (qry == 'total_pax'):
      qry = qrySwitch.to
    return 'SELECT ' + qry + "AND \"Year-Month-Day\" " + intv


am_df = pd.read_sql_query(text("SELECT DISTINCT ON (DATE_TRUNC('month', \"Year-Month-Day\")) DATE_TRUNC('month', \"Year-Month-Day\") AS month, SUM(\"Total Pax\")as pax, AVG(\"Yield\")as yield FROM cirium_traffic_northamerica WHERE \"Year-Month-Day\">= '2022-01-01' AND \"Orig\" IN ('LAX', 'SFO', 'DFW', 'IAH') AND \"Stop-1 Airport\" is null AND \"Total Pax\" >0 GROUP BY \"Year-Month-Day\" LIMIT 10000;"), conn)

am_df.plot(kind = 'line', x = 'month',y = 'pax', c = '#294173', legend = False)
plt.title('Monthly Total PAX')
plt.xlabel('date')
plt.ylabel('total pax')
plt.grid(axis = 'y', color = 'grey', linestyle = '--', linewidth = 0.5)
plt.savefig('sum_pax.png')
plt.show()

am_df.plot(kind = 'line', x = 'month', y= 'yield', c = '#294173', legend = False)
plt.title('Monthly Average Yields')
plt.xlabel('date')
plt.ylabel('Average Yields')
plt.grid(axis = 'y', color = 'grey', linestyle = '--', linewidth = 0.5)
plt.savefig('avg_yields.png')
plt.show()


am_df = pd.read_sql_query(text("SELECT DISTINCT ON (DATE_TRUNC('month', \"Year-Month-Day\")) DATE_TRUNC('month', \"Year-Month-Day\") AS month, SUM(\"Seats\") as seats FROM cirium_schedule_northamerica WHERE \"Year-Month-Day\">= '2022-01-01' AND \"Orig\" IN ('LAX', 'SFO', 'DFW', 'IAH') AND \"Dest\" IN ('SYD', 'MEL', 'BNE') AND \"Stop-1 Airport\" is null GROUP BY \"Year-Month-Day\" LIMIT 30000;"), conn)

am_df.plot(kind = 'line', x = 'month', y= 'seats', c = '#294173', legend = False)
plt.title('Monthly Total Seats')
plt.xlabel('month-year')
plt.ylabel('Total Seats')
plt.grid(axis = 'y', color = 'grey', linestyle = '--', linewidth = 0.5)
plt.savefig('sum_seats.png')
plt.ticklabel_format(style = 'Plain', axis = 'y')
plt.show()





qry = """SELECT
    DATE_TRUNC('month', \"Year-Month-Day\") as month,
    AVG(\"Yield\") as yield,
    SUM(\"Total Pax\") as pax
FROM cirium_traffic_northamerica
WHERE
    \"Orig\" IN ('LAX', 'SFO', 'DFW', 'IAH', 'HNL')
    AND \"Dest\" IN ('SYD', 'MEL', 'BNE')
	AND \"Op Al\" = ('UA')
	AND \"Stop-1 Airport\" is null
	AND \"Total Pax\" >0
    AND \"Year-Month-Day\">= '2022-01-01'
group by
  month"""

df = pd.read_sql_query(text(qry), conn)
#print(df)
# #Create a metadata object
# metadata = MetaData()

# # Reflect the database schema to get table and column information
# metadata.reflect(bind=engine)
  
# # Iterate through all tables and columns
# for table_name, table in metadata.tables.items():
#     if ('emission' in table_name or 'icao' in table_name or 'details' in table_name):
#         continue
#     for column in table.c:
#         print(f"Table: {table_name}, Column: {column.name}")
#         # print(f"Average: {avg_result}, Sum: {sum_result}")
