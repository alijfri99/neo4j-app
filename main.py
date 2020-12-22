from neo4j import GraphDatabase
from helper_functions import *

graphdb = GraphDatabase.driver(uri="bolt://localhost:7687", auth=("neo4j", "mypassword"))
session = graphdb.session()

search("Ali", "password", "bd", session)