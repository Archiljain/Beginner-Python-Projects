import time 
timestamp = time.strftime('%H:%M:%S', time.localtime())
print(timestamp)
if (timestamp>= '00:00:00' and timestamp<= '12:00:00'):
  print ("good morning")
elif (timestamp> '12:00:00' and timestamp<= '18:00:00'):
  print("good afternoon")
else:
  print("good night")
