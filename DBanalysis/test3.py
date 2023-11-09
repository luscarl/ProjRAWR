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

# # Define your PostgreSQL database connection
db_uri = 'postgresql://student003:chihrusvfnihdipp@dataviation-database-1.chl8zbfpbhhh.ap-southeast-2.rds.amazonaws.com/dataviation_tutorial'

# # Create an SQLAlchemy engine
engine = create_engine(db_uri, echo=False)
conn = engine.connect()

am_df = pd.read_sql_query(text("SELECT DISTINCT ON (DATE_TRUNC('month', \"Year-Month-Day\")) DATE_TRUNC('month', \"Year-Month-Day\") AS month, SUM(\"Total Pax\")as pax, AVG(\"Yield\")as yield FROM cirium_traffic_northamerica WHERE \"Year-Month-Day\">= '2022-01-01' AND \"Orig\" IN ('LAX') AND \"Stop-1 Airport\" is not null AND \"Total Pax\" >0 GROUP BY \"Year-Month-Day\" LIMIT 10000;"), conn)

am_df.plot(kind = 'line', x = 'month',y = 'pax', c = '#294173', legend = False)
plt.title('Monthly Total PAX')
plt.xlabel('date')
plt.ylabel('total pax')
plt.grid(axis = 'y', color = 'grey', linestyle = '--', linewidth = 0.5)
plt.savefig('sum_pax.png')

am_df.plot(kind = 'line', x = 'month', y= 'yield', c = '#294173', legend = False)
plt.title('Monthly Average Yields')
plt.xlabel('date')
plt.ylabel('Average Yields')
plt.grid(axis = 'y', color = 'grey', linestyle = '--', linewidth = 0.5)
plt.savefig('avg_yields.png')


am_df = pd.read_sql_query(text("SELECT DISTINCT ON (DATE_TRUNC('month', \"Year-Month-Day\")) DATE_TRUNC('month', \"Year-Month-Day\") AS month, SUM(\"Seats\") as seats FROM cirium_schedule_northamerica WHERE \"Year-Month-Day\">= '2022-01-01' AND \"Orig\" IN ('LAX') AND \"Stop-1 Airport\" is not null GROUP BY \"Year-Month-Day\" LIMIT 30000;"), conn)

am_df.plot(kind = 'line', x = 'month', y= 'seats', c = '#294173', legend = False)
plt.title('Monthly Total Seats')
plt.xlabel('month-year')
plt.ylabel('Total Seats')
plt.grid(axis = 'y', color = 'grey', linestyle = '--', linewidth = 0.5)
plt.savefig('sum_seats.png')

am_df = pd.read_sql_query(text("SELECT DISTINCT ON (DATE_TRUNC('month', \"Year-Month-Day\")) DATE_TRUNC('month', \"Year-Month-Day\") AS month, SUM(\"Total Pax\") as qf FROM cirium_traffic_northamerica WHERE \"Year-Month-Day\">= '2022-01-01' AND \"Orig\" IN ('YVR','LAX','IAH','DFW','SFO','JFK','SCL') AND \"Stop-1 Airport\" is not null AND \"Op Al\" IN ('QF') AND \"Total Pax\" >0 GROUP BY \"Year-Month-Day\" LIMIT 10000;"), conn)
am_df1 = pd.read_sql_query(text("SELECT DISTINCT ON (DATE_TRUNC('month', \"Year-Month-Day\")) DATE_TRUNC('month', \"Year-Month-Day\") AS month, SUM(\"Total Pax\") as va FROM cirium_traffic_northamerica WHERE \"Year-Month-Day\">= '2022-01-01' AND \"Orig\" IN ('YVR','LAX','IAH','DFW','SFO','JFK','SCL') AND \"Stop-1 Airport\" is not null AND \"Op Al\" IN ('VA') AND \"Total Pax\" >0 GROUP BY \"Year-Month-Day\" LIMIT 10000;"), conn)
# ax = am_df.plot(kind = 'line', x='month', y='qf', c= 'b', legend = False)
# am_df1.plot(ax=ax)
plt.title('Monthly Total PAX by airlines')
plt.xlabel('date')
plt.ylabel('total pax')
plt.grid(axis = 'y', color = 'grey', linestyle = '--', linewidth = 0.5)
plt.savefig('sum_qf.png')
am_df1.plot(kind = 'line', x='month', y='va',c= 'g', legend = False)
plt.title('Monthly Total PAX - VA')
plt.xlabel('date')
plt.ylabel('total pax')
plt.grid(axis = 'y', color = 'grey', linestyle = '--', linewidth = 0.5)
plt.savefig('sum_va.png')
print(am_df)
print(am_df1)

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
print(df)
