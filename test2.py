import psycopg2

conn = psycopg2.connect(
    host = "dataviation-database-1.chl8zbfpbhhh.ap-southeast-2.rds.amazonaws.com",
    database = "dataviation_tutorial",
    user = "student003",
    password = "chihrusvfnihdipp"
    )

cursor = conn.cursor()
e_str = "SELECT SUM(\"Total Pax\") FROM cirium_traffic_asia WHERE \"Orig\" in ('CMB', 'RML', 'HRI', 'JAF') AND \"Year\" = 2022"
cursor.execute(e_str)

print(e_str)
print(cursor.fetchall())

