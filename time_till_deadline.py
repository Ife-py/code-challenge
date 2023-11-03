from  datetime import datetime
"""this is a program that asks for your proposed target and gives you a countdown till that days or time"""
 
user_input=input("enter your goal with a deadline seperated with a colon\n")
input_list=user_input.split(":")

goal=input_list[0] 
deadline=input_list[1]

deadline_date=datetime.strptime(deadline,"%d.%m.%Y")
#calculate how many days from now till deadline
today_date=datetime.today()
date_past=today_date-deadline_date
hours_past=int(date_past.total_seconds()/60/60)
minutes_past=int(date_past.total_seconds()/60)
seconds_past=int(date_past.total_seconds())
time_till=deadline_date-today_date
hours_till=int(time_till.total_seconds()/60/60) 
minutes=int(time_till.total_seconds()/60)
seconds=int(time_till.total_seconds())
time=input("enter if your time to be calculated is future or past\n")
if time== "future":
    validation=input("enter what you want the unit deadline to be; hours,minutes,seconds\n")
    if validation =="hours": 
        print(f"Dear user! Time remaining for your goal:{goal} is {hours_till} hours")
    elif validation=="minutes":
        print(f"Dear user! Time remaining for your goal: {goal} is {minutes} minutes")
    elif validation=="seconds":
        print(f"Dear user! Time remaining for your goal:{goal} is {seconds} seconds")    
elif time=="past":
    valid=input("enter what you want the unit deadline to be; hours,minutes,seconds\n")
    if valid =="hours": 
        print(f"Dear user! you have spent {hours_past}  hours for your goal:{goal} till date ")
    elif valid=="minutes":
        print(f"Dear user! you have spent {minutes_past} minutes for your goal: {goal} till date")
    elif valid=="seconds":
        print(f"Dear user!you have spent {seconds_past} seconds for your goal :{goal} till date")
                