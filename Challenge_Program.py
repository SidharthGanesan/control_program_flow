from datetime import datetime, date


#print(datetime.now())
date1=datetime.now()
date3=str(datetime.now())
date2=datetime.strftime(date1,"%m-%d-%Y %H:%M:%S")
print(date1,date2)
strifedyear=date1.strftime("%Y")
#print(strifed)
strifedmonth=date1.strftime("%m")
strifeddate=date1.strftime("%d")

print("+"*20)
print(date1.strftime("%d%m%Y"))
print("+"*20)
print(strifedyear+'/'+strifedmonth+'/'+strifeddate)
#print("+"*20)
#print(strifeddate+"/"+strifedmonth+"/"+strifedyear)
#print("+"*20)
#print(strifeddate+strifedmonth+strifedyear)
#print("+"*20)
date2=date1.date()
print("***" * 5)
print(date2)
#age = int(input("Enter your date of birth(format : DDMMYYYY)"))
#min=int(x)
#max=int(y)
#x=
#strDate ='Sun Jan 22 21:32:58 +0000 2012'
#objDate = datetime.strptime(strDate, '%a %b %d %H:%M:%S +%f %Y')

#print(objDate)
#2019-04-29 14:30:53

name= str(input("Please enter your name"))
dtob = str(input("please enter the Date_Time of birth in DD-MM-YYYY HH:MM format :"))
convert_DTOB= datetime.strptime(dtob,"%d-%m-%Y %H:%M:%S")
convert_DTOB1=datetime.strptime(dtob,"%d-%m-%Y %H:%M:%S")
print(convert_DTOB1)
print(type(convert_DTOB))