from sqlalchemy import (Column, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class Instances(Base):
    __tablename__ = "instances"
    id = Column(Integer, primary_key=True)
    instanceId = Column(String(250), nullable=False)
    instanceType = Column(String(250), nullable=False)
    architecture = Column(String(250), nullable=False)
    status = Column(String(250), nullable=False)


engine = create_engine(
    'postgresql://postgres:admin@localhost/aws-instances')
Base.metadata.create_all(engine)
