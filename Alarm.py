# define day time and weekends
day_time = 6.30
is_weekend = day_time < 6.30

#set the condition for wake up time and weekend

if is_weekend:
    print("Sleep in (it's weekend!)")

elif day_time >= 6.30:
    print(f"Wake up at {day_time:.2f}")  # Format for two decimal places
else:
    print("Sleep in")