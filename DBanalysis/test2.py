import psycopg2

conn = psycopg2.connect(
    host = "dataviation-database-1.chl8zbfpbhhh.ap-southeast-2.rds.amazonaws.com",
    database = "dataviation_tutorial",
    user = "student003",
    password = "chihrusvfnihdipp"
    )

cursor = conn.cursor()
e_str = "SELECT * FROM cirium_traffic_europe LIMIT 10"
cursor.execute(e_str)

print(e_str)
print(cursor.fetchone())

