from Time import Time

t1 = Time(0, 0, 0)
t2 = Time(6, 30, 18)
t3 = Time(12, 59, 59)
t4 = Time(20, 9, 64)

print("time 1:", t1.toString())
print("time 2:", t2.toString())
print("time 3:", t3.toString())
print("time 4:", t4.toString())

print("time 2 hours:", t2.getHours())
print("time 3 hours:", t3.getHours())
print("time 1 minutes:", t1.getMinutes())
print("time 4 minutes:", t4.getMinutes())
print("time 3 seconds:", t3.getSeconds())
print("time 1 seconds:", t1.getSeconds())

print("time 3 in seconds:", t3.timeInSeconds())
print("time 1 in seconds:", t1.timeInSeconds())
print("time 4 in seconds:", t4.timeInSeconds())

t1.changeTheTime(0, 18, 33)
t4.changeTheTime(18, 9, 10)
print("new time 1:", t1.toString())
print("new time 4:", t4.toString())

print("time 1 in 12 hour format:", t1.twelveHourClock())
print("time 2 in 12 hour format:", t2.twelveHourClock())
print("time 3 in 12 hour format:", t3.twelveHourClock())
print("time 4 in 12 hour format:", t4.twelveHourClock())

print("time 1 general time:", t1.whatTimeIsIt())
print("time 2 general time:", t2.whatTimeIsIt())
print("time 3 general time:", t3.whatTimeIsIt())
print("time 4 general time:", t4.whatTimeIsIt())

print("time 2 compared to time 4:", t2.compareTo(t4))
print("time 3 compared to time 1:", t3.compareTo(t1))
print("time 1 compared to time 1:", t1.compareTo(t1))

print("time 1 time until time 4:", t1.timeTill(t4).toString())
print("time 2 time until time 3:", t2.timeTill(t3).toString())
