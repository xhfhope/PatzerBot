#Join Team Patzer! Get in the game on Chess.com We have our own club for special events. https://www.chess.com/club/2100-patzer-lane?ref_id=1376596
#"Coach is going to be stoked! Thanks for subscribing. Sub Love in the chat!"


import cfg
import socket
import time
import re
import random
from datetime import datetime

def chat(sock, msg):
    sock.send("PRIVMSG {} :{}\r\n".format(cfg.CHAN, msg).encode("utf-8"))
    #print('SENT: ' + msg)
    
def ban(sock, user):
    chat(sock, ".ban {}".format(user))

def unban(sock, user):
    chat(sock, ".unban {}".format(user))

def timeout(sock, user, secs=600):
    chat(sock, ".timeout {}{}".format(user + ' ', secs))

CHAT_MSG=re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

# network functions go here

s = socket.socket()
s.connect((cfg.HOST, cfg.PORT))
s.send("PASS {}\r\n".format(cfg.PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(cfg.NICK).encode("utf-8"))
s.send("JOIN {}\r\n".format(cfg.CHAN).encode("utf-8"))

queue = []

try:
    while True:
        try:
            response = s.recv(1024).decode("utf-8")
            if response == "PING :tmi.twitch.tv\r\n":
                s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
            else:
                try:
                    username = re.search(r"\w+", response).group(0) # return the entire match
                    username = username.lower()
                    message = CHAT_MSG.sub("", response)
                    if username in cfg.trustedList:
                        if message[:4] == '!add':                        
                            print('#########################################################################################' + message)
                            userToAdd = message[5:]
                            userToAdd = userToAdd[:-1]
                            queue.append(userToAdd)
                            
                        if message[:6] == '!queue':                    
                                i = 1
                                st = ''
                                for user in queue:
                                    st = st + str(i) + ') ' + user + ', '
                                    i = i + 1
                                if len(queue)>0:
                                    st = st[:-2]
                                chat(s,st)
                                
                        if message[:4] == '!pop':
                            if len(queue)>0:                            
                                del queue[0]                            

                        if message[:5] == '!love':
                            spamCount=3
                            curMsg=''
                            if message[5].isdigit():
                                spamCount = int(message[5])
                                if spamCount > 5:
                                    spamCount=5
                            for i in range(0,spamCount):
                                curMsg+='chessc22100patzerlane '
                                chat(s,curMsg)                        
                            for i in range(spamCount,1,-1):
                                curMsg = curMsg[:-22]
                                chat(s,curMsg)
                                
                        if message[:5] == '!join':
                            chat(s, "Join Team Patzer! Get in the game on Chess.com We have our own club for special events. https://www.chess.com/club/2100-patzer-lane?ref_id=1376596")
                            
                        if message[:10] == '!challenge':
                            chat(s, "https://www.chess.com/live#challenge=5m5s&member=shootfilm?ref_id=1376596")
                            
                        if message[:7] == '!3check':
                            chat(s,'https://www.chess.com/live#challenge=3m2s%7Cthreecheck&member=shootfilm?ref_id=1376596')
                            
                        if message[:6] == '!arena':
                            chat(s,"https://www.chess.com/live#r=21940?ref_id=1376596")
                            
                        if message[:9] == '!bughouse':
                            chat(s,"https://www.chess.com/live#challenge=3m2s%7Cbughouse&member=shootfilm?ref_id=1376596")
                            
                        if message[:9] == '!chess960':
                            chat(s,"https://www.chess.com/live#challenge=3m2s%7Cchess960&member=shootfilm?ref_id=1376596")
                            
                        if message[:4] == '!h&b':
                            chat(s,"https://www.chess.com/live#challenge=10m5s&member=shootfilm?ref_id=1376596")
                            
                        if message[:11] == '!tournament':
                            chat(s,"Join the club! https://www.chess.com/club/2100-patzer-lane?ref_id=1376596 Today's Event: BHappy Birthday https://www.chess.com/live#t=924155?ref_id=1376596")
                            
                        if message[:8] == '!sponsor':
                            chat(s,"Coach plays on chess.com , this is because they have been gracious enough to sponsor the stream! Sign up now if you haven't already! :D")
                            
                        if message[:6] == '!prime':
                            chat(s,"If you have Amazon Prime you can now subscribe to our channel every month for free! https://twitch.amazon.com/prime for more info https://www.twitch.tv/subs/chesscoachnet")
                            
                        if message[:3] == '!og':
                            chat(s,"MrBigBizzness 1st Tier 3 Sub 12/31/17, Mattychess20 1st Tier 1 Sub 11/20/17, Mattychess20 1st Tier 2 Sub 12/6/17, JayChess730 #1 Moderator 12/20/17")
                            
                        if message[:5] == '!koth':
                            chat(s,"https://www.chess.com/live#challenge=3m2s%7Ckingofthehill&member=shootfilm?ref_id=1376596")
                            
                except AttributeError:
                    print('attribute error')
        except UnicodeDecodeError:
            print('unicodedecodeerror')
                
except KeyboardInterrupt:
    print('done')
