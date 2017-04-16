
# this file is used to configure the connection to database, modify it
# when installing the app. You should create the Database before launching the app

config = {
    "DB_ENGINE": "postgresql",
    "DB_NAME": "aws-instances",
    "DB_USER": "postgres",
    "DB_PWD": "admin",
    "DB_HOST": "localhost"
}


def buildConnector():
    connector = str()
    connector = connector + config["DB_ENGINE"] + "://"
    connector = connector + config["DB_USER"] + ":"
    connector = connector + config["DB_PWD"] + "@"
    connector = connector + config["DB_HOST"] + "/"
    connector = connector + config["DB_NAME"]
    return connector

