from app import db
from datetime import datetime
import requests
import json
def test_fetch() -> dict:
    parks = [
        {"name": "yellowstone", "description": "maybe exists idk", "stateAbbr": "HI"}
    ]
    return parks

def get_parks() -> dict:
    conn = db.connect()
    query_res = conn.execute("SELECT name, description, stateAbbr, directionsUrl FROM Parks LIMIT 10;").fetchall() # Use Python's .format() for user input
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

def search_parks_by_name(search_query) -> dict:
    search_query = "%" + search_query + "%"
    conn = db.connect()
    query = "SELECT name, description, stateAbbr, directionsUrl FROM Parks WHERE name LIKE %s LIMIT 10;"
    query_res = conn.execute(query, (search_query)).fetchall()
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

def search_parks_by_state(search_query) -> dict:
    search_query = "%" + search_query + "%"
    conn = db.connect()
    query = "SELECT name, description, stateAbbr, directionsUrl FROM Parks WHERE stateAbbr LIKE %s LIMIT 10;"
    query_res = conn.execute(query, (search_query)).fetchall()
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


def get_events() -> dict:
    conn = db.connect()
    query = """SELECT title, e1.description, name, stateAbbr, datestart, dateend, eventid
               FROM Parks p1 JOIN Events e1 ON (p1.name = e1.parkfullname)
               ORDER BY title
               LIMIT 20;"""
    query_res = conn.execute(query).fetchall()
    conn.close()
    events = []
    for res in query_res:
        item = {
            "event_title": res[0],
            "event_description": res[1] if len(res[1]) < 200 else res[1][:200] + "...",
            "park_name": res[2],
            "states": res[3],
            "start_date": res[4],
            "end_date": res[5],
            "event_id": res[6]
        }
        events.append(item)
    return events

def get_events_free_parking() -> dict:
    conn = db.connect()
    query = """SELECT title, e1.description, name, stateAbbr, datestart, dateend
                FROM Parks p1 JOIN Events e1 ON (p1.name = e1.parkfullname)
                WHERE name NOT IN (SELECT p.name
                                   FROM Parks p JOIN ParkingLots l ON(p.parkCode = l.parkCode)
                                   WHERE hasFee=True)
                ORDER BY datestart;"""
    query_res = conn.execute(query).fetchall()
    free_parking_events = []
    conn.close()
    for res in query_res:
        free_parking_events.append(res[0])
    return free_parking_events

def in_season_activities(input) -> dict:
    arg = input
    conn = db.connect()
    query = """SELECT p.name, p.description, p.stateAbbr, count(a.activID), season
                FROM Activities a JOIN Parks p ON (a.parkCode = p.parkCode)
                WHERE season = %s AND a.hasFee = false GROUP BY a.parkCODE
                ORDER BY count(a.activID) DESC
                LIMIT 10;"""
    query_res = conn.execute(query, arg).fetchall()
    conn.close()
    parks = []
    for res in query_res:
        item = {
            "name": res[0],
            "description": res[1],
            "states": res[2],
            "amount": res[3]
        }
        parks.append(item)
    return parks

def get_activities() -> dict:
    conn = db.connect()
    query = """SELECT a.title, a.description, a.season, p.name, p.stateAbbr, a.hasFee
                FROM Activities a JOIN Parks p ON (a.parkCode = p.parkCode)
                ORDER BY a.title
                LIMIT 10;"""
    query_res = conn.execute(query).fetchall() # Use Python's .format() for user input
    conn.close()
    parks = []
    for res in query_res:
        item = {
            "name": res[0],
            "description": res[1],
            "season": res[2],
            "park": res[3],
            "state": res[4],
            "fee": res[5]
        }
        parks.append(item)
    return parks

def get_amenities() -> dict:
    conn = db.connect()
    query = """SELECT a.name, p.name, p.stateAbbr
                FROM Amenities a JOIN Parks p ON (a.parkCode = p.parkCode)
                ORDER BY p.name
                LIMIT 10;"""
    query_res = conn.execute(query).fetchall() # Use Python's .format() for user input
    conn.close()
    parks = []
    for res in query_res:
        item = {
            "name": res[0],
            "park": res[1],
            "state": res[2]
        }
        parks.append(item)
    return parks

def amenities_by_park(search_query) -> dict:
    search_query = "%" + search_query + "%"
    conn = db.connect()
    query = """SELECT a.name, p.name, p.stateAbbr
                FROM Amenities a JOIN Parks p ON (a.parkCode = p.parkCode)
                WHERE p.name LIKE %s
                ORDER BY p.name
                LIMIT 10;"""
    query_res = conn.execute(query, (search_query)).fetchall()
    conn.close()
    parks = []
    for res in query_res:
        item = {
            "name": res[0],
            "park": res[1],
            "state": res[2]
        }
        parks.append(item)
    return parks

def activities_by_state(search_query) -> dict:
    search_query = "%" + search_query + "%"
    conn = db.connect()
    query = """SELECT a.title, a.description, a.season, p.name, p.stateAbbr, a.hasFee
                FROM Activities a JOIN Parks p ON (a.parkCode = p.parkCode)
                WHERE p.stateAbbr LIKE %s
                ORDER BY a.title
                LIMIT 10;"""
    query_res = conn.execute(query, (search_query)).fetchall()
    conn.close()
    parks = []
    for res in query_res:
        item = {
            "name": res[0],
            "description": res[1],
            "season": res[2],
            "park": res[3],
            "state": res[4],
            "fee": res[5]
        }
        parks.append(item)
    return parks

def activities_by_season(search_query) -> dict:
    conn = db.connect()
    query = """SELECT a.title, a.description, a.season, p.name, p.stateAbbr, a.hasFee
                FROM Activities a JOIN Parks p ON (a.parkCode = p.parkCode)
                WHERE a.season = %s
                ORDER BY a.title
                LIMIT 10;"""
    query_res = conn.execute(query, (search_query)).fetchall()
    conn.close()
    parks = []
    for res in query_res:
        item = {
            "name": res[0],
            "description": res[1],
            "season": res[2],
            "park": res[3],
            "state": res[4],
            "fee": res[5]
        }
        parks.append(item)
    return parks

def activities_by_name(search_query) -> dict:
    search_query = "%" + search_query + "%"
    conn = db.connect()
    query = """SELECT a.title, a.description, a.season, p.name, p.stateAbbr, a.hasFee
                FROM Activities a JOIN Parks p ON (a.parkCode = p.parkCode)
                WHERE a.title LIKE %s
                ORDER BY a.title
                LIMIT 10;"""
    query_res = conn.execute(query, (search_query)).fetchall()
    conn.close()
    parks = []
    for res in query_res:
        item = {
            "name": res[0],
            "description": res[1],
            "season": res[2],
            "park": res[3],
            "state": res[4],
            "fee": res[5]
        }
        parks.append(item)
    return parks


def get_parknames() -> dict:
    conn = db.connect()
    query_res = conn.execute("SELECT name FROM Parks;").fetchall() #LIMIT 2
    park_name = []
    conn.close()
    for res in query_res:
        item = {
            "name": res[0]
        }
        park_name.append(item)
    return park_name

def insert_new_event(title, description, start_date, end_date, park_name):
    eventid = "eventid:" + str(datetime.now())
    conn = db.connect()
    query = "INSERT INTO Events (eventid, title, description, datestart, dateend, parkfullname) VALUES(%s, %s, %s, %s, %s, %s);"#.format(
        #title, description, start_date, end_date, park_name)
    query_res = conn.execute(query, eventid, title, description, start_date, end_date, park_name)
    conn.close()

def delete_event(event_id):
    conn = db.connect()
    query = "DELETE FROM Events WHERE eventid = %s"
    query_res = conn.execute(query, event_id)
    print("AYO: ", query_res)
    conn.close()

def edit_event(event_id, title, description, start_date, end_date):
    conn = db.connect()
    query = "UPDATE Events SET title = %s, description = %s, datestart = %s, dateend = %s WHERE eventid = %s"
    query_res = conn.execute(query, title, description, start_date, end_date, event_id)
    conn.close()

def search_events(search_query) -> dict:
    search_query = "%" + search_query + "%"
    conn = db.connect()
    query = """SELECT title, e1.description, name, stateAbbr, datestart, dateend, eventid
               FROM Parks as p1 JOIN Events e1 ON (p1.name = e1.parkfullname)
               WHERE p1.name LIKE %s
               ORDER BY title
               LIMIT 100;"""
    query_res = conn.execute(query, (search_query)).fetchall()
    conn.close()
    events = []
    for res in query_res:
        item = {
            "event_title": res[0],
            "event_description": res[1] if len(res[1]) < 200 else res[1][:200] + "...",
            "park_name": res[2],
            "states": res[3],
            "start_date": res[4],
            "end_date": res[5],
            "event_id": res[6]
        }
        events.append(item)
    return events

def update_events_from_api():
    query = "INSERT OR UPDATE INTO Events(eventid, title, description, datestart, dateend, parkfullname, category, hasFee) VALUES"
    api_url = "https://developer.nps.gov/api/v1/events?limit=1000&api_key=3V7MT57J6LMTqfiona1k5RC6x8SHxCVGzSC0Km9j&pagesize=50"
    api_params = {'pagenumber': 1}
    api_data = requests.get(url=api_url, params=api_params).json()
    #
    #https://developer.nps.gov/api/v1/events?limit=1000&api_key=3V7MT57J6LMTqfiona1k5RC6x8SHxCVGzSC0Km9j
    """1`datestart` VARCHAR(1024),
        1`description` VARCHAR(1024),
        `category` VARCHAR(1024),
        1`eventid` VARCHAR(1024) PRIMARY KEY,
        1`dateend` VARCHAR(1024),
        1`parkfullname` VARCHAR(1024) REFERENCES Parks(name),
        1`title` VARCHAR(1024),
        `image` VARCHAR(1024),
        `hasFee` BOOL"""
    num_events = int(api_data['total'])
    event_data = api_data['data']
    print("hi", num_events, len(event_data))
    i = 0
    while i < num_events:
        #do the thing
        for event in event_data[:1]:
            #do a thing
            #print(event)
            #+ event['title'] + 
            query = query + "(\"" + event['id'] + "\", \"" + "e" + "\", \"" + event['description'] + "\", \"" + event['datestart'] + "\", \"" + event['dateend'] + "\", \"" + event['parkfullname'] + "\", \"" + event['category'] + "\", " + str(event['isfree'] == "false") + "),"
            i += 1
        
        #check if we need new events
        print("buffering: ", i, ". pageno: ", api_params['pagenumber'])
        
        #just try first one
        break

        num_events = int(api_data['total'])
        if num_events == 0:
            break

        #get new events
        api_params['pagenumber'] += 1
        api_data = requests.get(url=api_url, params=api_params).json()
        event_data = api_data['data']
    query = query[:-1] + ";"
    print("master oogway", i, "query: ", query)
    
    # for i in range(num_events):
    #     event = event_data[i]
    #     query = query + "(),"
    # query[-1] = ';'
    # return
    conn = db.connect()
    query_res = conn.execute(query)
    print(query_res)
    conn.close()
    