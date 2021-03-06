import os
import socket
import logging

HEADER_VER_1='snmptrap -v 1 -c %s %s %s %s %s %s '
HEADER_VER_2='snmptrap -v 2c -c %s %s %s '
UPTIME='30'

class snmpHandler:
      """This class will take a snmptrap command line utility."""
      def __init__(self, dataCollector):
          self.dataCollector=dataCollector

      def sendEvent(self, msg, type, community, version, utf_8=True):
          """This method will take a message, a type (snmptrap), version(1 or 2c)
          and community name, then send out a snmptrap."""
          if type=='snmptrap':
              if version=='2c':
                  myHead=HEADER_VER_2 % (community, self.dataCollector, UPTIME)
                  cmd=myHead+msg
              elif version=='1':
                  localhost=socket.gethostbyname(socket.gethostname())
                  msgList=msg.split(' ')
                  newMsg=' '.join(msgList[3:])
                  myHead=HEADER_VER_1 % (community, self.dataCollector, msgList[0], localhost, ' '.join(msgList[1:3]), UPTIME)
                  cmd=myHead+newMsg
              logging.debug(cmd)
              os.system(cmd)

      def close(self):
          pass


