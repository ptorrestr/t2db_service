import daemon_connector.m_socket as m_socket
import json

class DictionaryArgument(object):
    def __init__(self):
        self.lan = {"consumer":"_consumer", "consumer_secret" : "_consumer_sec",
                "access":"_access", "access_secret":"_access_sec",
                "query":"_query", "search_id":"_process_id"}

    def getTranslation(self, word):
        return self.lan[word]

    def getArguments(self, data, operation):
        args = {}
        args['_command'] = operation
        dataKeys = data.keys()
        for dataKey in dataKeys:
            try:
                args[self.getTranslation(dataKey)] = data[dataKey]
            except Exception as e:
                continue
        return args

class DaemonConnection(object):
    
    def send(self, args):
        #TODO error handling
        #print(args)
        sock = m_socket.control_socket()
        sock.connect("leftraru", 8081)
        sock.send(args)
        resp = sock.recv()
        #print (resp)

class DaemonSearch(object):
   
    def newEntry(self, data):
        args = DictionaryArgument().getArguments(data, "START")
        DaemonConnection().send(args)
    
    def updateEntry(self, data):
        #TODO not implemented yet
        args = DictionaryArgument().getArguments(data, "UPDATE")
    
    def pollEntry(self, data):
        #TODO not implemented yet
        args = DictionaryArgument().getArguments(data, "POLL")

    def deleteEntry(self, data):
        args = DictionaryArgument().getArguments(data, "DELETE")
        DaemonConnection().send(args)
