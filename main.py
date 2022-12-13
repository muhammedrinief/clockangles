def timeToAngle(time):
	try:
		# take input as xx:yy and split by ":"
		[hours, minutes] = time.split(":")
		hours = int(hours)
		minutes = int(minutes)
		# filter out invalid times (24 hour format)
		if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
			exit()
		# calculations still done according to a 12h analog clock
		#convert 24h to 12h
		hours %= 12
		# 1 hour = 30 degrees + 0.5 degrees per minute
		hdegree = (hours * 30) + (minutes * 0.5)
		# 1 minute = 6 degrees
		mdegree = (minutes * 6)
		# positive of difference in degrees
		deg = abs(hdegree - mdegree)
		# return shortest angle
		return min(deg, 360 - deg)
		# handle errors from invalid input
	except:
		print("invalid time")
		exit()

time = input("enter a time: ")
print(str(timeToAngle(time)) + "°")
