wake_up_time = 7.00  # You can set this to any time

day_time = wake_up_time
is_weekend = wake_up_time < 7.00

#if weekend

if is_weekend:
    print("Is weekend (it's weekend!)")

elif day_time >= wake_up_time:
    print(f"Wake up at {wake_up_time:.2f}")  # Format for two decimal places
else:
    print("Sleep in")