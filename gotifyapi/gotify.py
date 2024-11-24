import requests
import json


class Gotify(object):
    def __init__(self, **settings):
        self.fqdn = settings['fqdn']
        self.session = requests.Session()
        self.token = settings['token']
        self.headers = {"Content-Type": "application/json",
                        "X-Gotify-Key": "{}".format(settings['token'])}

    def getapplications(self):
        return self.__httphandler(method="GET",
                                  endpoint="/application")

    def getmessages(self):
        return self.__httphandler(method="GET",
                                  endpoint="/message?token={}".format(self.token))

    def postmessage(self, **message):
        data = {'message': message['alert'],
                'priority': message['priority'],
                'title': message['title']}
        return self.__httphandler(method="POST",
                                  endpoint="/message",
                                  body=json.dumps(data))

    def delmessage(self, id=None):
        return self.__httphandler(method="DELETE",
                                  msgid=id)

    def __error(self, exception=None):
        raise Exception("Error:{}".format(exception))

    def httpstatuscode(self, httpcode=None):
        if httpcode == 200:
            pass
        elif httpcode == 201:
            pass
        elif httpcode == 400:
            pass
        else:
            pass

    def __httphandler(self, **http):
        if http['method'] == "GET":
            try:
                res = self.session.get(self.fqdn + http['endpoint'],
                                       headers=self.headers)
                return res.json()
            except Exception as e:
                self.__error(exception=e)
        elif http['method'] == "POST":
            try:
                res = self.session.post(self.fqdn + http['endpoint'],
                                        headers=self.headers,
                                        data=http['body'])
                return res.json()
            except Exception as e:
                self.__error(exception=e)
        elif http['method'] == "PUT":
            try:
                return self.session.put(self.fqdn + http['endpoint'],
                                        headers=self.headers)
            except Exception as e:
                self.__error(exception=e)
        elif http['method'] == "DELETE":
            try:
                return self.session.put(self.fqdn + http['endpoint'],
                                        headers=self.headers)
            except Exception as e:
                self.__error(exception=e)
