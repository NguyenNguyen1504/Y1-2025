time_used = int(input("How many minutes has the device been charging for? \n"))
charged = int(input("How many percentage points did the charge increase during this period? \n"))
speed = charged / time_used
current = int(input("What is the current battery percentage? \n"))
time_left = (100 - current) / speed
print(f"Charging speed (%/min): {speed}")
print(f"Minutes until full: {time_left}")