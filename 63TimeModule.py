# 63 Time Module in python [05:29:33]-----------------------------------------
# epoch = a date and time from which a computer measures system time. When your coputer thinks that time began
import time
print(time.ctime(0)) #convert a time expressed in seconds since epoch to a readable string
print(time.ctime(100000))
print(time.time()) #Return current seconds since epoch
print(time.ctime(time.time()))
# ----------------------
time_object = time.localtime()
print(time_object)
local_time = time.strftime("%d %B %Y %H:%M:%S",time_object) 
print(local_time)
# --------------------------
time_string="20 April, 2020"
time_object=time.strptime(time_string,"%d %B, %Y")
print(time_object)
# ------------------------------------------------
# There is a format of it..
# (year, month, day, hours, minutes, secs, #day of the year, dst)
time_tuple=(2020,4,20,4,20,0,0,0,0)
time_string=time.asctime(time_tuple)
print(time_string)
# ----------------------------
# There is a format of it..
# (year, month, day, hours, minutes, secs, #day of the year, dst)
time_tuple=(2020,4,20,4,20,0,0,0,0)
time_string=time.mktime(time_tuple)
print(time_string)