import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy import MetaData
from os import environ
import matplotlib.pyplot as plt

# Define your PostgreSQL database connection
db_uri = 'postgresql://student003:chihrusvfnihdipp@dataviation-database-1.chl8zbfpbhhh.ap-southeast-2.rds.amazonaws.com/dataviation_tutorial'

# Create an SQLAlchemy engine
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



<<<<<<< HEAD
am_df = pd.read_sql_query(text("SELECT DISTINCT ON (DATE_TRUNC('month', \"Year-Month-Day\")) DATE_TRUNC('month', \"Year-Month-Day\") AS month, SUM(\"Total Pax\") FROM cirium_traffic_northamerica WHERE \"Year-Month-Day\">= '2022-01-01' AND \"Total Pax\" >0 GROUP BY \"Year-Month-Day\" LIMIT 30000;"), conn)
print(am_df)
plot = am_df.plot(kind = 'line', x = 'month',y = 'sum', legend = False)
=======
am_df = pd.read_sql_query(text("SELECT DISTINCT ON (DATE_TRUNC('month', \"Year-Month-Day\")) DATE_TRUNC('month', \"Year-Month-Day\") AS month, SUM(\"Total Pax\"), AVG(\"% POO Orig\") as avg FROM cirium_traffic_northamerica WHERE \"Year-Month-Day\">= '2022-01-01' AND \"Total Pax\" >0 GROUP BY \"Year-Month-Day\" LIMIT 10000;"), conn)
am_df.plot(kind = 'line', x = 'month',y = 'sum', legend = False)
>>>>>>> fee9d1fa51544317b105c4355cf230cecc38dfa5
plt.title('Monthly Total PAX')
plt.xlabel('date')
plt.ylabel('total pax')
plt.grid(True)
plt.savefig('sum_pax.png')
plt.show()

plt.title('Monthly Average %POO Origin')
am_df.plot(x = 'month', y= 'avg', legend = False)
plt.title('Monthly Average %poo origin')
plt.xlabel('date')
plt.ylabel('average %poo origin')
plt.savefig('avg_pooorig.png')
plt.show()

am_df = pd.read_sql_query(text("SELECT DISTINCT ON (DATE_TRUNC('month', \"Year-Month-Day\")) DATE_TRUNC('month', \"Year-Month-Day\") AS month, AVG(\"Yield\") FROM cirium_traffic_northamerica WHERE \"Year-Month-Day\">= '2022-01-01' AND \"Yield\" >0 GROUP BY \"Year-Month-Day\" LIMIT 30000;"), conn)
print(am_df)
plot = am_df.plot(kind = 'line', x = 'month',y = 'sum', legend = False)
plt.title('Monthly Total PAX')
plt.xlabel('date')
plt.ylabel('average yield')
plt.grid(True)
plt.show()
plt.savefig('testing.png')

am_df = pd.read_sql_query(text("SELECT DISTINCT ON (DATE_TRUNC('month', \"Year-Month-Day\")) DATE_TRUNC('month', \"Year-Month-Day\") AS month, SUM(\"Seats\") FROM cirium_traffic_northamerica WHERE \"Year-Month-Day\">= '2022-01-01' AND \"Seats\" >0 GROUP BY \"Year-Month-Day\" LIMIT 30000;"), conn)
print(am_df)
plot = am_df.plot(kind = 'line', x = 'month',y = 'sum', legend = False)
plt.title('Monthly Total PAX')
plt.xlabel('date')
plt.ylabel('total seats')
plt.grid(True)
plt.show()
plt.savefig('testing.png')

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
