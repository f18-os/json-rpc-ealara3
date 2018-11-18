# minimalistic client example from
# https://github.com/seprich/py-bson-rpc/blob/master/README.md#quickstart

import socket
from bsonrpc import JSONRpc
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
	JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)
from node import *
import json

# Cut-the-corners TCP Client:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50001))

rpc = JSONRpc(s,framing_cls=JSONFramingNone)
server = rpc.get_peer_proxy()


############# creating the tree
leaf1 = node("leaf1")						#create a node with no children
leaf2 = node("leaf2")						#create a node with no children

root = node("root", [leaf1, leaf1, leaf2])	#create a node with a children as leaf1, leaf1 and leaf2

print("graph before increment")
root.show()

# do this increment remotely:
increment(root)

print("graph after increment")
root.show()

GraphRoot = CreateDict(root)

#print("HERE ", GraphRoot.keys())
dictSend = json.dumps(GraphRoot)	  			#makes the dictionary into a a json string to send
print(server.nop(dictSend))

# Execute in server:
result = server.swapper('Hello World!')
# "!dlroW olleH"
print(result)

print(server.nop({1:[2,3]}))


rpc.close() # Closes the socket 's' also
