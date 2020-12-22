from neo4j import GraphDatabase
from helper_functions import *

graphdb = GraphDatabase.driver(uri="bolt://localhost:7687", auth=("neo4j", "mypassword"))
session = graphdb.session()
logged_in = False

username = None
password = None

while True:
    text = input(">")
    text = list(map(str, text.split()))

    if text[0].lower() == "signup" and len(text) == 3:
        if not logged_in:
            logged_in = signup(text[1], text[2], session)
            if logged_in:
                username = text[1]
                password = text[2]
        else:
            print("Please Log Out Before Trying To Sign Up.")

    elif text[0].lower() == "login" and len(text) == 3:
        if not logged_in:
            logged_in = login(text[1], text[2], session)
            if logged_in:
                username = text[1]
                password = text[2]
        else:
            print("Please Log Out Before Trying To Log In.")

    elif text[0].lower() == "add" and len(text) == 3:
        if logged_in:
            add(username, password, text[1], text[2], session)
        else:
            print("Please Log In First.")

    elif text[0].lower() == "show" and len(text) == 1:
        if logged_in:
            show(username, password, session)
        else:
            print("Please Log In First.")

    elif text[0].lower() == "delete" and len(text) == 2:
        if logged_in:
            delete(username, password, text[1], session)
        else:
            print("Please Log In First.")

    elif text[0].lower() == "search" and len(text) == 2:
        if logged_in:
            search(username, password, text[1], session)
        else:
            print("Please Log In First.")

    elif text[0].lower() == "logout" and len(text) == 1:
        if logged_in:
            logged_in = False
            username = None
            password = None
            print("Logged Out Successfully.")
        else:
            print("Invalid Command.")

    elif text[0].lower() == "exit" and len(text) == 1:
        break

    else:
        print("Invalid Command")