from datetime import datetime

#grabs current time and date
time = datetime.now()

#format for time
date = time.strftime("%B %d, %Y")


print(f"today is {date}")

