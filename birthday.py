"""
birthday.py
Author: nathalie
Credit: googled for elif info
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name 
todaymonth = datetime.today().month
todaydate = datetime.today().day

name = str(input("Hello, what is your name? "))
birthMonth = str(input("Hi " + name + ", what was the name of the month you were born in? ")) 

fall = ["September", "October", "November"] 
winter = ["December", "January", "February"]
spring = ["March", "April", "May"]
summer = ["June", "July", "August"] 


if birthMonth in winter:
    Season = "winter"
elif birthMonth in spring: 
    Season = "spring"   
elif birthMonth in summer: 
    Season = "summer"
elif birthMonth in fall:
    Season = "fall"

yrofbirth = int(input("And what year were you born in, " + name + "? ")) 


eighties = [1980, 1981, 1982, 1983, 1984, 
1985, 1986, 1987, 1988, 1989] #you know the 80s


nineties = [1990, 1991, 1992, 1993, 1994, 1995,
1996, 1997, 1998, 1999]


Thousands = [2000, 2001, 2002, 2003, 2004, 2005,
2006, 2007, 2008, 2009, 2010] 

if yrofbirth in eighties:
    Era = "eighties"
elif yrofbirth in nineties: 
    Era = "nineties"
elif yrofbirth in Thousands:
    Era = "two thousands"
else : 
    Era = "stone age"
dob = str(input("And the day? ")) 

if int(dob) == todaydate and month_name[int(todaymonth)] == birthMonth: 
    print("Happy birthday!") 
elif birthMonth == "October" and int(dob) == 31: 
    print("You were born on Halloween!") 
else: 
    print(name + ", you are a "+ Season + " baby of the " + Era +".") 