#Timer Generator
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

#Had to use AI to find the issue with dividing by the minutes then by hours per day to switch to a 24-hour cycle. 
total_minutes = mins + dura
new_hour = (hour + total_minutes // 60) % 24
new_minute = total_minutes % 60

print(new_hour, ":", new_minute, sep="")

#Checked and it does reset back to 0 after 24 hours due to useing modulus operator.