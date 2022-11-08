from pymongo import MongoClient
import pywhatkit
import datetime
def message():
    client = MongoClient(port=27017)
    db = client.messages
    x = db.messages.find_one()
    now=datetime.datetime.now()
    message = x["Message"]
    phone="+91"+x["Phone"]
    time = int(x["Time"])
    hour=now.hour
    minute=now.minute
    if (minute+time)>60:
        hour+=1
        minute=(minute+time)-60
    else:
        minute+=time
    if time==1:
        second=now.second
        second=60-second
        pywhatkit.search("timer for "+str(second)+ "seconds")
    elif time==2:
        time=time-1
        time*=60
        second=now.second
        second=60-second
        second+=time
        pywhatkit.search("timer for "+str(second)+" seconds")
    elif time==3:
        time=time-1
        time*=60
        second=now.second
        second=60-second
        second+=time
        pywhatkit.search("timer for "+str(second)+" seconds")
    elif time==5:
        time=time-1
        time*=60
        second=now.second
        second=60-second
        second+=time
        pywhatkit.search("timer for "+str(second)+" seconds")
    else:
        time=time-1
        time*=60
        second=now.second
        second=60-second
        second+=time
        pywhatkit.search("timer for "+str(second)+" seconds")
    pywhatkit.sendwhatmsg(phone, message, hour, minute)
    db.messages.delete_many({})
