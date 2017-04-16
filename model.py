from db import *
from config import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# connect with the database
engine = create_engine("postgresql://postgres:admin@localhost/aws-instances")

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

session = DBSession()

# CRUD methods for aws-instances


def addInstance(instance):
    # check if instance already exists
    if not getOneInstance(instance["InstanceId"]):
        new_instance = Instances(instanceId=instance["InstanceId"],
                                 instanceType=instance["InstanceType"],
                                 architecture=instance["Architecture"],
                                 status=instance["State"]["Name"])
        session.add(new_instance)
        session.commit()


def addInstancesBundle(reservationList):
    for reservation in reservationList:
        for instance in reservation['Instances']:
            addInstance(instance)


def delInstance(instanceId):
    instance = getOneInstance(instanceId)
    if instance:
        session.delete(instance)
        session.commit()


def getAllInstances():
    return session.query(Instances).all()


def getOneInstance(instanceId):
    return session.query(Instances).filter_by(instanceId=instance).all()
