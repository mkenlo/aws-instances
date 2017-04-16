from db import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# connect with the database
engine = create_engine(
    'postgresql://postgres:admin@localhost/aws-instances')
# create a connection between the database and the class from database_setup

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

session = DBSession()

# CRUD methods for aws-instances


def addInstance():
    pass


def delInstance():
    pass


def getInstances():
    pass


def getOneInstance():
    pass


