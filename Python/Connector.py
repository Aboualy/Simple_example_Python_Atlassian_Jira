import requests
from jira import JIRA


class Connector:
    def __init__(self, server, email, pwd):
        self.server = server
        self.email = email
        self.pwd = pwd

    def getContent(self):
        return JIRA(self.server,
                    basic_auth=(self.email, self.pwd))