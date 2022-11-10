from app import db

def search_name():
    return "None"

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
            i = i.replace(")", "")
            if state.get(i) == None:
                state[i] = 1
                if i != None:
                    states.append(i)
    return states