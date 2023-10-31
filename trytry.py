import pandas as pd

from sqlalchemy import create_engine, text
from sqlalchemy import MetaData
import matplotlib.pyplot as plt

# # Define your PostgreSQL database connection
db_uri = 'postgresql://student003:chihrusvfnihdipp@dataviation-database-1.chl8zbfpbhhh.ap-southeast-2.rds.amazonaws.com/dataviation_tutorial'

# # Create an SQLAlchemy engine
engine = create_engine(db_uri, echo=False)
conn = engine.connect()

am_df = pd.read_sql_query(text("SELECT DISTINCT ON (DATE_TRUNC('month', \"Year-Month-Day\")) DATE_TRUNC('month', \"Year-Month-Day\") AS month, SUM(\"Total Pax\") as qf FROM cirium_traffic_northamerica WHERE \"Year-Month-Day\">= '2022-01-01' AND \"Orig\" IN ('YVR','LAX','IAH','DFW','SFO','JFK','SCL') AND \"Stop-1 Airport\" is null AND \"Op Al\" IN ('QF') AND \"Total Pax\" >0 GROUP BY \"Year-Month-Day\" LIMIT 10000;"), conn)
am_df1 = pd.read_sql_query(text("SELECT DISTINCT ON (DATE_TRUNC('month', \"Year-Month-Day\")) DATE_TRUNC('month', \"Year-Month-Day\") AS month, SUM(\"Total Pax\") as va FROM cirium_traffic_northamerica WHERE \"Year-Month-Day\">= '2022-01-01' AND \"Orig\" IN ('YVR','LAX','IAH','DFW','SFO','JFK','SCL') AND \"Stop-1 Airport\" is null AND \"Op Al\" IN ('VA') AND \"Total Pax\" >0 GROUP BY \"Year-Month-Day\" LIMIT 10000;"), conn)

print(am_df)
print(am_df1)
result = pd.merge(am_df, am_df1, how="outer")
print(result)

plt.plot(result.month, result.qf)
plt.plot(result.month, result.va, c= 'b')
plt.legend(['qf','va'])
plt.title('Monthly Total PAX by airlines')
plt.xlabel('date')
plt.ylabel('total pax')
plt.grid(axis = 'y', color = 'grey', linestyle = '--', linewidth = 0.5)
plt.savefig('sum_paxAL.png')