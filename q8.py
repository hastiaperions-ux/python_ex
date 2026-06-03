from datetime import datetime , timedelta

start_str = input("Enter start time (YYYY-MM-DD HH:MM:SS): ").strip()
end_str = input("Enter end time (YYYY-MM-DD HH:MM:SS): ").strip()

current = datetime.strptime(start_str, "%Y-%m-%d %H:%M:%S")
end = datetime.strptime(end_str, "%Y-%m-%d %H:%M:%S")

op_minutes = 0
while current < end:
    if not (0 <= current.hour < 6):
        op_minutes += 1  
        
    current += timedelta(minutes=1)  

op_hours = timedelta(minutes=op_minutes)
print("Op hours:", op_hours)
print(current)