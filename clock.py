current_time_str= input("What is the current time?")
future_time_str= input("In how many hours do you want your alarm to set off?")

current_time_str= float(current_time_str)
future_time_str= float(future_time_str)

clock=(current_time_str + future_time_str)
alarm= clock%24

print(alarm)