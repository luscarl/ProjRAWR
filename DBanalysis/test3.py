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


am_df = pd.read_sql_query(text("SELECT DISTINCT ON (DATE_TRUNC('month', \"Year-Month-Day\")) DATE_TRUNC('month', \"Year-Month-Day\") AS month, SUM(\"Total Pax\"), AVG(\"% POO Orig\")as avg, AVG(\"Rev\") as rev FROM cirium_traffic_northamerica WHERE \"Year-Month-Day\">= '2022-01-01' AND \"Total Pax\" >0 GROUP BY \"Year-Month-Day\" LIMIT 10000;"), conn)
am_df.plot(kind = 'line', x = 'month',y = 'sum', legend = False)

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

am_df.plot(x = 'month', y = 'rev', legend = False)
plt.title('Monthly average revenue')
plt.xlabel('date')
plt.ylabel('average revenue')
plt.savefig('avg_rev.png')
plt.show()

doc = SimpleDocTemplate("document.pdf", pagesize=letter, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=18)
story = []

styles = getSampleStyleSheet()
title = "My PDF Document"
story.append(Paragraph(title, styles["Title"]))
story.append(Spacer(1, 12))

text = "This is some text content that we're adding to our PDF document. You can customize formatting using styles."
story.append(Paragraph(text, styles["Normal"]))
# story.append(PageBreak())

story.append(Paragraph("this is the avg poo origin idc"))
image_path = "avg_pooorig.png"  # Replace with the path to your image file
img = Image(image_path)
story.append(img)

story.append(Paragraph("this is the avg revenue of northamerica"))
story.append(Image("avg_rev.png", width = 300, height = 200))
story.append(Paragraph("this is the sum of passengers from of northamerica"))
story.append(Image("sum_pax.png", width = 300, height = 200))

doc.build(story)

# #Create a metadata object
# metadata = MetaData()

# # Reflect the database schema to get table and column information
# metadata.reflect(bind=engine)


# # Iterate through all tables and columns
# for table_name, table in metadata.tables.items():
#     if ('emission' in table_name or 'icao' in table_name or 'details' in table_name):
#         continue
#     for column in table.c:
#         if ('cirium_traffic_northamerica' in table_name):
#            print('0')