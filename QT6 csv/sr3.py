import sqlite3


def arrival(*arg, sort=True) -> list:
    db = sqlite3.connect("duties.db")
    cur = db.cursor()
    result = cur.execute(f"""SELECT
      p.name,
      f.fee * c.ratio
    FROM 
      People p,
      Cities c,
      Fees f
    WHERE
      p.city_id = c.id  
    AND
      c.city IN {arg}
    AND
      p.reason_id = f.id
    ORDER BY f.fee * c.ratio DESC, p.name;""")
    result = list(result)
    db.close()
    if sort:
        return result
    else:
        return sorted(result, key=lambda x: x[1])


data = ['Tabriz', 'Edirne', 'Venice', 'Baghdad', 'Qom',
        'Isfahan', 'Kashan', 'Adrianople', 'Sivas']
print(*arrival(*data, sort=False), sep='\n')
