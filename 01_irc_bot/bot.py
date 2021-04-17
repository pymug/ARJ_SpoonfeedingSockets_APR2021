"""
Abdur-Rahmaan Janhangeer
Skeleton of https://github.com/pyhoneybot/honeybot/
"""

import time
import os
import socket

directory = "irc"
if not os.path.exists(directory):
    os.makedirs(directory)
target = open(os.path.join(directory, "log.txt"), "w")


def message_checker(msgLine):
    sendvar = ""
    global mute
    mute = False
    completeLine = str(msgLine[1:]).replace("'b", "").split(":", 1)
    info = completeLine[0].split()
    message = (completeLine[1].split("\\r")[0]).replace("'b", "")
    sender = info[0][2:].split("!", 1)[0]
    refinedmsg = str(message.lower())
    refinedmsgl = len(refinedmsg)

    print("Complete Line-->" + str(completeLine))
    print("Info-->" + str(info))
    print("Message-->" + str(message))
    print("Sender-->" + str(sender) + "\n")


def ping_checker(pingLine):
    if pingLine.find(bytes("PING", "utf8")) != -1:
        pingLine = pingLine.rstrip().split()
        if pingLine[0] == bytes("PING", "utf8"):
            irc.send(bytes("PONG ", "utf8") + pingLine[1] + bytes("\r\n", "utf8"))


BOT_IRC_SERVER = "chat.freenode.net"
BOT_IRC_CHANNEL = "##bottestingmu"
# BOT_IRC_CHANNEL = "#python"
BOT_IRC_PORT = 6667
BOT_NICKNAME = "appinventormuBot"
# BOT_PASSWORD = ''


irc = socket.socket()


irc.connect((BOT_IRC_SERVER, BOT_IRC_PORT))
irc.recv(4096)


irc.send(bytes("NICK " + BOT_NICKNAME + "\r\n", "utf8"))
ping_checker(irc.recv(4096))
irc.send(
    bytes(
        "USER appinventormuBot appinventormuBot appinventormuBot : appinventormuBot IRC\r\n",
        "utf8",
    )
)
ping_checker(irc.recv(4096))
# irc.send(bytes('msg NickServ identify ' + BOT_PASSWORD + " \r\n"  ,'utf8')  )
# ping_checker(irc.recv(4096))
# irc.send(bytes('NICKSERV  identify ' + BOT_NICKNAME+' '+BOT_PASSWORD+ '\r\n','utf8'  )  )
# ping_checker(irc.recv(4096))
time.sleep(3)
irc.send(bytes("JOIN " + BOT_IRC_CHANNEL + "\r\n", "utf8"))


while 1:
    pass
    line = irc.recv(4096)
    print(line)
    ping_checker(line)
    if (
        line.find(bytes("PRIVMSG", "utf8")) != -1
        or line.find(bytes("NOTICE", "utf8")) != -1
    ):
        message_checker(line)
        target.write(str(line))
        target.flush()
