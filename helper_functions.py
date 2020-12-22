def signup(username, password, session):
    result = session.run("MATCH(n:User) WHERE n.username = '" + username + "' RETURN n;")
    if result.peek() is not None:
        print("Username already exists.")
        return False
    else:
        session.run("CREATE(n:User{username: '" + username + "', password: '" + password + "'});")
        return True


def login(username, password, session):
    result = session.run("MATCH(n:User) WHERE n.username = '" + username + "' RETURN n;")
    if result.peek() is None:
        print("Invalid Username.")
        return False
    else:
        result = session.run("MATCH(n:User) WHERE n.username = '" + username + "' AND n.password = '" + password +
                             "' RETURN n;")
        if result.peek() is None:
            print("Invalid Password.")
            return False
        else:
            return True


def add(username, password, name, number, session):
    result = session.run("MATCH(n:User)-[:Saved]->(m:Contact) WHERE (m.name = '" + name + "' OR m.number = '" + number +
                         "') AND n.username = '" + username + "' AND n.password = '" + password + "' RETURN m;")
    if result.peek() is not None:
        print("Contact Already Exists.")
        return False
    else:
        session.run("MATCH(n:User) WHERE n.username = '" + username + "' AND n.password = '" + password +
                    "' CREATE(m:Contact{name: '" + name + "', number: '" + number + "'})<-[:Saved]-(n);")
        print("Contact Added Successfully.")
        return True


def show(username, password, session):
    result = session.run("MATCH(m:Contact)<-[:Saved]-(n:User) WHERE n.username = '" + username + "' AND n.password = '"
                         + password + "' RETURN m.name AS name, m.number AS number;")
    if result.peek() is None:
        print("No Contact Found.")
        return
    else:
        for record in result:
            print("Name: " + record['name'] + ", Number: " + record['number'])