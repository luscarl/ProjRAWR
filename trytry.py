import pandas as pd

from sqlalchemy import create_engine, text
from sqlalchemy import MetaData
import matplotlib.pyplot as plt

# # Define your PostgreSQL database connection
db_uri = 'postgresql://student003:chihrusvfnihdipp@dataviation-database-1.chl8zbfpbhhh.ap-southeast-2.rds.amazonaws.com/dataviation_tutorial'

# # Create an SQLAlchemy engine
engine = create_engine(db_uri, echo=False)
conn = engine.connect()

am_df = pd.read_sql_query(text("SELECT DISTINCT ON (DATE_TRUNC('month', \"Year-Month-Day\")) DATE_TRUNC('month', \"Year-Month-Day\") AS month, SUM(\"Total Pax\") as qf FROM cirium_traffic_northamerica WHERE \"Year-Month-Day\">= '2022-01-01' AND \"Orig\" IN ('LAX', 'SFO', 'DFW', 'IAH') AND \"Stop-1 Airport\" is null AND \"Op Al\" IN ('QF') AND \"Total Pax\" >0 GROUP BY \"Year-Month-Day\" LIMIT 10000;"), conn)
am_df1 = pd.read_sql_query(text("SELECT DISTINCT ON (DATE_TRUNC('month', \"Year-Month-Day\")) DATE_TRUNC('month', \"Year-Month-Day\") AS month, SUM(\"Total Pax\") as aa FROM cirium_traffic_northamerica WHERE \"Year-Month-Day\">= '2022-01-01' AND \"Orig\" IN ('LAX', 'SFO', 'DFW', 'IAH') AND \"Stop-1 Airport\" is null AND \"Op Al\" IN ('AA') AND \"Total Pax\" >0 GROUP BY \"Year-Month-Day\" LIMIT 10000;"), conn)
am_df2 = pd.read_sql_query(text("SELECT DISTINCT ON (DATE_TRUNC('month', \"Year-Month-Day\")) DATE_TRUNC('month', \"Year-Month-Day\") AS month, SUM(\"Total Pax\") as ua FROM cirium_traffic_northamerica WHERE \"Year-Month-Day\">= '2022-01-01' AND \"Orig\" IN ('LAX', 'SFO', 'DFW', 'IAH') AND \"Stop-1 Airport\" is null AND \"Op Al\" IN ('UA') AND \"Total Pax\" >0 GROUP BY \"Year-Month-Day\" LIMIT 10000;"), conn)
am_df3 = pd.read_sql_query(text("SELECT DISTINCT ON (DATE_TRUNC('month', \"Year-Month-Day\")) DATE_TRUNC('month', \"Year-Month-Day\") AS month, SUM(\"Total Pax\") as dl FROM cirium_traffic_northamerica WHERE \"Year-Month-Day\">= '2022-01-01' AND \"Orig\" IN ('LAX', 'SFO', 'DFW', 'IAH') AND \"Stop-1 Airport\" is null AND \"Op Al\" IN ('DL') AND \"Total Pax\" >0 GROUP BY \"Year-Month-Day\" LIMIT 10000;"), conn)

print(am_df)
print(am_df1)
print(am_df2)
print(am_df3)

dfs = [am_df, am_df1, am_df2, am_df3]
dfs = [df.set_index('month') for df in dfs]
result=dfs[0].join(dfs[1:])

print(result)

plt.plot(result)
plt. legend(['QF','AA','UA','DL'])
plt. title('Monthly Total PAX by airlines')
plt.xlabel('date')
plt. ylabel('total pax')
plt. grid(axis= 'y', color= 'grey', linestyle = '--', linewidth = 0.5)
plt.savefig('sum_paxAL.png')



am_df = pd.read_sql_query(text("SELECT DISTINCT ON (DATE_TRUNC('month', \"Year-Month-Day\")) DATE_TRUNC('month', \"Year-Month-Day\") AS month, AVG(\"Yield\")as qf FROM cirium_traffic_northamerica WHERE \"Year-Month-Day\">= '2022-01-01' AND \"Orig\" IN ('LAX', 'SFO', 'DFW', 'IAH') AND \"Stop-1 Airport\" is null AND \"Op Al\" IN ('QF') AND \"Total Pax\" >0 GROUP BY \"Year-Month-Day\" LIMIT 10000;"), conn)
am_df1 = pd.read_sql_query(text("SELECT DISTINCT ON (DATE_TRUNC('month', \"Year-Month-Day\")) DATE_TRUNC('month', \"Year-Month-Day\") AS month, AVG(\"Yield\")as aa FROM cirium_traffic_northamerica WHERE \"Year-Month-Day\">= '2022-01-01' AND \"Orig\" IN ('LAX', 'SFO', 'DFW', 'IAH') AND \"Stop-1 Airport\" is null AND \"Op Al\" IN ('AA') AND \"Total Pax\" >0 GROUP BY \"Year-Month-Day\" LIMIT 10000;"), conn)
am_df2 = pd.read_sql_query(text("SELECT DISTINCT ON (DATE_TRUNC('month', \"Year-Month-Day\")) DATE_TRUNC('month', \"Year-Month-Day\") AS month, AVG(\"Yield\")as ua FROM cirium_traffic_northamerica WHERE \"Year-Month-Day\">= '2022-01-01' AND \"Orig\" IN ('LAX', 'SFO', 'DFW', 'IAH') AND \"Stop-1 Airport\" is null AND \"Op Al\" IN ('UA') AND \"Total Pax\" >0 GROUP BY \"Year-Month-Day\" LIMIT 10000;"), conn)
am_df3 = pd.read_sql_query(text("SELECT DISTINCT ON (DATE_TRUNC('month', \"Year-Month-Day\")) DATE_TRUNC('month', \"Year-Month-Day\") AS month, AVG(\"Yield\")as dl FROM cirium_traffic_northamerica WHERE \"Year-Month-Day\">= '2022-01-01' AND \"Orig\" IN ('LAX', 'SFO', 'DFW', 'IAH') AND \"Stop-1 Airport\" is null AND \"Op Al\" IN ('DL') AND \"Total Pax\" >0 GROUP BY \"Year-Month-Day\" LIMIT 10000;"), conn)

print(am_df)
print(am_df1)
print(am_df2)
print(am_df3)

dfs = [am_df, am_df1, am_df2, am_df3]
dfs = [df.set_index('month') for df in dfs]
answer=dfs[0].join(dfs[1:])

print(answer)

plt.plot(answer)
plt. legend(['QF','AA','UA','DL'])
plt. title('Monthly Average Yield by airlines')
plt.xlabel('date')
plt. ylabel('average yield')
plt. grid(axis= 'y', color= 'grey', linestyle = '--', linewidth = 0.5)
plt.savefig('avg_yieldAL.png')


am_df = pd.read_sql_query(text("SELECT DISTINCT ON (DATE_TRUNC('month', \"Year-Month-Day\")) DATE_TRUNC('month', \"Year-Month-Day\") AS month, SUM(\"Seats\") as qf FROM cirium_schedule_northamerica WHERE \"Year-Month-Day\">= '2022-01-01' AND \"Orig\" IN ('LAX', 'SFO', 'DFW', 'IAH') AND \"Stop-1 Airport\" is null AND \"Op Al\" IN ('QF') GROUP BY \"Year-Month-Day\" LIMIT 10000;"), conn)
am_df1 = pd.read_sql_query(text("SELECT DISTINCT ON (DATE_TRUNC('month', \"Year-Month-Day\")) DATE_TRUNC('month', \"Year-Month-Day\") AS month, SUM(\"Seats\") as aa FROM cirium_schedule_northamerica WHERE \"Year-Month-Day\">= '2022-01-01' AND \"Orig\" IN ('LAX', 'SFO', 'DFW', 'IAH') AND \"Stop-1 Airport\" is null AND \"Op Al\" IN ('AA') GROUP BY \"Year-Month-Day\" LIMIT 10000;"), conn)
am_df2 = pd.read_sql_query(text("SELECT DISTINCT ON (DATE_TRUNC('month', \"Year-Month-Day\")) DATE_TRUNC('month', \"Year-Month-Day\") AS month, SUM(\"Seats\") as ua FROM cirium_schedule_northamerica WHERE \"Year-Month-Day\">= '2022-01-01' AND \"Orig\" IN ('LAX', 'SFO', 'DFW', 'IAH') AND \"Stop-1 Airport\" is null AND \"Op Al\" IN ('UA') GROUP BY \"Year-Month-Day\" LIMIT 10000;"), conn)
am_df3 = pd.read_sql_query(text("SELECT DISTINCT ON (DATE_TRUNC('month', \"Year-Month-Day\")) DATE_TRUNC('month', \"Year-Month-Day\") AS month, SUM(\"Seats\") as dl FROM cirium_schedule_northamerica WHERE \"Year-Month-Day\">= '2022-01-01' AND \"Orig\" IN ('LAX', 'SFO', 'DFW', 'IAH') AND \"Stop-1 Airport\" is null AND \"Op Al\" IN ('DL') GROUP BY \"Year-Month-Day\" LIMIT 10000;"), conn)

print(am_df)
print(am_df1)
print(am_df2)
print(am_df3)

dfs = [am_df, am_df1, am_df2, am_df3]
dfs = [df.set_index('month') for df in dfs]
final=dfs[0].join(dfs[1:])

print(final)

plt.plot(final)
plt. legend(['QF','AA','UA','DL'])
plt. title('Monthly Total Seats by airlines')
plt.xlabel('date')
plt. ylabel('total seats')
plt. grid(axis= 'y', color= 'grey', linestyle = '--', linewidth = 0.5)
plt.savefig('sum_seatsAL.png')