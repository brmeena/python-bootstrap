import math
import sys
import traceback
sys.path.append("../")
from datetime import datetime
def getDateDifferenceInSeconds(date1,date2):
    #print(date1,date2)
    date_diff=(date1-date2).total_seconds()
    #print(date_diff)
    return date_diff

def getDateDifferenceInHours(date1,date2):
    date_diff_seconds= getDateDifferenceInSeconds(date1,date2)
    return date_diff_seconds/3600

def getDateDifferenceInDays(date1,date2):
    date_diff_hours= getDateDifferenceInHours(date1,date2)
    return math.floor(date_diff_hours/24)


def getStartDate(date_object):
    date_object=datetime.combine(date_object,datetime.min.time())
    return date_object

def formatDate(dateObj,format):
    dateObj=dateObj.strftime(format)
    return dateObj

