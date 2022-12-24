from database.database import get_db

class UserService():
    @staticmethod
    def register_collection(weight, description, users_id, materials_id):
      db = get_db()
      try:
          result = db.execute('''
              INSERT INTO collections (weight, description, users_id, materials_id)
              VALUES (?, ?, ?, ?)
          ''', [weight, description, users_id, materials_id])
          db.commit()
          return result.lastrowid
      except Exception:
          #if collection is received, return collection id (inserted id), else return -1
          return -1

    @staticmethod
    def get_collections():
      db = get_db()
      return db.execute('''
        SELECT cid, users_id, weight, price as pricePerUnit, (weight*price) as total_price, received, added, materials_id, name, pid FROM (
          SELECT DENSE_RANK() OVER (PARTITION BY cid ORDER BY (JULIANDAY(received)-JULIANDAY(added))) as rank, (JULIANDAY(received)-JULIANDAY(added)) as datediff, * FROM (
            SELECT
                c.id as cid, c.weight, c.received, c.users_id, c.materials_id, m.name, p.id as pid, p.price, p.added
            FROM collections as c
            INNER JOIN materials as m
                on m.id = c.materials_id
            INNER JOIN prices as p
                ON p.materials_id = c.materials_id AND p.added <= c.received
          ) as t1 order by cid, rank
        ) as t2 WHERE rank = 1
      ''').fetchall()

    @staticmethod
    def get_collections_by_user(user_id):
      db = get_db()
      return db.execute('''
        SELECT cid, users_id, weight, price as pricePerUnit, (weight*price) as total_price, received, added, materials_id, name, pid FROM (
          SELECT DENSE_RANK() OVER (PARTITION BY cid ORDER BY (JULIANDAY(received)-JULIANDAY(added))) as rank, (JULIANDAY(received)-JULIANDAY(added)) as datediff, * FROM (
            SELECT
                c.id as cid, c.weight, c.received, c.users_id, c.materials_id, m.name, p.id as pid, p.price, p.added
            FROM collections as c
            INNER JOIN materials as m
                on m.id = c.materials_id
            INNER JOIN prices as p
                ON p.materials_id = c.materials_id AND p.added <= c.received
          ) as t1 order by cid, rank
        ) as t2 WHERE rank = 1 AND users_id = ?
      ''', [user_id]).fetchall()