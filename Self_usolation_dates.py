import re
import datetime

def Self_isolation_end_date(startDate,duration):
  if (re.match('^\d{1,2}-\d{1,2}-\d{2,4}', startDate) or re.match('^\d{1,2}/\d{1,2}/\d{2,4}', startDate)) :
    date = re.split(r'\D',startDate)
    currentDate = datetime.datetime(int('20'+date[2][-2:]),int(date[0]),int(date[1]))
    currentDate = currentDate + datetime.timedelta(days = duration)
    end_date =(currentDate.day,currentDate.month,currentDate.year)
    return end_date
  else :
    return '00/00/0000'
     

print(Self_isolation_end_date('3-02-2022',7))
print(Self_isolation_end_date('03-2-2022',7))
print(Self_isolation_end_date('03-2-22',365))
print(Self_isolation_end_date('3/02/2022',7))
print(Self_isolation_end_date('03/2/2022',7))
print(Self_isolation_end_date('03/2/22',365))

