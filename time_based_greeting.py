#time based greeting and current date and time
import datetime
start_time = datetime.datetime.now()
i=start_time.strftime("%H")
print("Good Morning" if int(i)<12 else "Good Afternoon" if int(i)<16 else "Good Evening" if int(i)<20 else "Good Night")
print("Date:",start_time.strftime("%d-%m-%Y "),"Day:",start_time.strftime("%A "),"Time:",start_time.strftime("%H:%M:%S")  )