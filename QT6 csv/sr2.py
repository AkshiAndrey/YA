import sqlite3

location_ = tuple(input())
db = sqlite3.connect("native.db")
cur = db.cursor()
result = cur.execute(f"""SELECT
  place
FROM 
  places p
WHERE
  p.location IN {location_}
ORDER BY p.how_far DESC;""")
for i in result:
    print(i[0])
db.close()
