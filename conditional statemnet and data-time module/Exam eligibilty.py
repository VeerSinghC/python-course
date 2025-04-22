working_days = int(input("Enter total number of working days: "))
absent_days = int(input("Enter total number of days absent: "))

attended_days = working_days - absent_days
attendance_percentage = (attended_days / working_days) * 100

print(f"Attendance Percentage: {attendance_percentage:.2f}%")
if attendance_percentage < 75:
    print("You are not allowed to sit in the exam.")
else:
    print("You are allowed to sit in the exam.")
