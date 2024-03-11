import sqlite3

lst_ = []
genre = input()
db = sqlite3.connect("music_db.sqlite")
cur = db.cursor()
result = cur.execute(f"""SELECT DISTINCT
  al.title
FROM 
  genre g,
  track t,
  album al,
  artist a
WHERE
  t.genreid = g.genreid 
AND
  t.albumid = al.albumid
AND
  al.artistid = a.artistid
AND
  g.name = 'Opera'
ORDER BY al.title;""")
for i in result:
    if i[0] not in lst_:
        lst_.append(i[0])
for i in lst_:
    print(i)
db.close()