from app import db
import sys

def test_fetch() -> dict:
    parks = [
        {"name": "yellowstone", "description": "maybe exists idk", "stateAbbr": "HI"}
    ]
    return parks

def fetch_parks() -> dict:
    conn = db.connect()
    query_res = conn.execute("SELECT name, description, stateAbbr, directionsUrl FROM Parks ORDER BY name ASC, stateAbbr ASC LIMIT 10;").fetchall() # Use Python's .format() for user input
    conn.close()
    parks = []
    for res in query_res:
        item = {
            "name": res[0],
            "description": res[1],
            "states": res[2],
            "directions": res[3]
        }
        parks.append(item)
    return parks

def search_parks(input):
    conn = db.connect()
    input = str(input)
    print(f"Input2: {input}", file=sys.stderr)
    query = f"SELECT name, description, stateAbbr, directionsUrl FROM Parks WHERE name LIKE %s ORDER BY name ASC, stateAbbr ASC LIMIT 10;"
    args = [input+'%']
    query_res = conn.execute(query, args).fetchall() # Use Python's .format() for user input
    conn.close()
    parks = []
    for res in query_res:
        item = {
            "name": res[0],
            "description": res[1],
            "states": res[2],
            "directions": res[3]
        }
        parks.append(item)
    return parks

def get_activities():
    conn = db.connect()
    results = conn.execute("Select DISTINCT title from Activities")
    conn.close()
    activities = []
    for result in results:
        activities.append(result[0])
    return activities

def get_states():
    conn = db.connect()
    results = conn.execute("Select DISTINCT stateAbbr from Parks")
    conn.close()
    state = {}
    states = []
    for result in results:
        for i in str(result).split(","):
            i = i.replace("'", "")
            i = i.replace("(", "")
            if state.get(i) == None:
                state[i] = 1
                if i != ")":
                    states.append(i)
    return states