import psycopg2
import sys

conn = psycopg2.connect(
    host = "dataviation-database-1.chl8zbfpbhhh.ap-southeast-2.rds.amazonaws.com",
    database = "dataviation_tutorial",
    user = "student003",
    password = "chihrusvfnihdipp"
    )

cursor = conn.cursor()
e_str = "SELECT * FROM cirium_traffic_europe LIMIT 10"
cursor.execute(e_str)

pax_22JAN =  "BETWEEN \'2023-03-01 00:00:00\' AND \'2023-06-02 00:00:00\'"


def intervalGenerator(interval, year, num):
    month = ''
    if (interval == 'mon'):
        if (num > 12 & num < 1):
            return 0
        if (num >= 10 & num <= 12):
            month = str(num) + '-01'
        else:
            month = str(year) + '-' + month
    return str(year) + '-'

def qryGenerator(interval, year, num):
    return "BETWEEN " + "''" + " AND " + "''"

print(cursor.fetchall())
