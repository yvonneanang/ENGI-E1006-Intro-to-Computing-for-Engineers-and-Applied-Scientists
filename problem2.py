#submitted by Yvonne Naa Ardua Anang (uni: yna2103)
# completed by Mikaela Zhang(uni:xz2782) and Yvonne Naa Ardua Anang (uni:yna2103)


input_in_seconds = int(input ("Please type time in seconds:"))
hour = input_in_seconds//3600
remainder_hour = input_in_seconds%3600
minute = remainder_hour//60
second = remainder_hour%60

if hour == 1:
    x = "hour"
else:
    x = "hours"

if minute == 1:
    y = "minute"
else:
    y = "minutes"

if second == 1:
    z = "second"
else:
    z = "seconds"

print ("{} {}, {} {}, {} {}".format (hour,x, minute,y, second,z))