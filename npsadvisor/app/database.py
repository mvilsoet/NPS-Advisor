from app import db
def test_fetch() -> dict:
    parks = [
        {"name": "yellowstone", "description": "maybe exists idk", "stateAbbr": "HI"}
    ]
    return parks

def fetch_parks() -> dict:
    conn = db.connect()
    query_res = conn.execute("SELECT name, description, stateAbbr FROM Parks LIMIT 10;").fetchall() # Use Python's .format() for user input
    conn.close()
    parks = []
    for res in query_res:
        item = {
            "name": res[0],
            "description": res[1],
            "states": res[2]
        }
        parks.append(item)
    return parks
