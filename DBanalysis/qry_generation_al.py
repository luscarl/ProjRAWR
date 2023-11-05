import pandas as pd
from sqlalchemy import text
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select

# # Define your PostgreSQL database connection
db_uri = 'postgresql://student003:chihrusvfnihdipp@dataviation-database-1.chl8zbfpbhhh.ap-southeast-2.rds.amazonaws.com/dataviation_tutorial'

# # Create an SQLAlchemy engine
engine = create_engine(db_uri, echo=False)
conn = engine.connect()

