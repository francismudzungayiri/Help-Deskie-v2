import random
import string
import datetime as dt



def getTicketNumber():
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(12))
    return result_str



def getFormattedDateNow():
    return dt.datetime.now()

    
def getDate(date):
    now = dt.datetime.strftime(date,'%d/%m/%Y')
    return now
    
    
def getTime(date):
    nowTime = dt.datetime.strftime(date,"%H:%M:%S")
    return nowTime
    
    
    