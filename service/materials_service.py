from database.database import get_db

class MaterialsService():
    @staticmethod
    def get_current_prices():
        db = get_db()
        return db.execute('''
        SELECT materials.id, materials.name, prices.price, prices.added FROM materials
	        INNER JOIN (SELECT materials_id, MAX(id) as pid FROM prices GROUP BY materials_id) as latest_prices ON latest_prices.materials_id = materials.id
          INNER JOIN prices ON prices.id = latest_prices.pid
        ''').fetchall()
    
    def get_stats():
        db = get_db()
        return db.execute('''
          SELECT materials_id, materials.name, MAX(received) as latest_received, AVG(weight) as average_weight
            FROM collections
            INNER JOIN materials ON materials.id = collections.materials_id
            GROUP BY materials_id
        ''').fetchall()