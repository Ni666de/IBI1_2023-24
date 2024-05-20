from matplotlib import pyplot as plt

student_day = {
    "Sleeping": 8,
    "Classes": 6,
    "Studying": 3.5,
    "TV": 2,
    "Music": 1,
    "Other": 0  
}

total_hours = 24

student_day["Other"] = total_hours - sum(student_day.values())

print("Average Day of a University Student:")
print(student_day)

plt.figure(figsize=(8, 8))
plt.pie(student_day.values(), labels=student_day.keys(), autopct='%1.1f%%')
plt.title("Pie Chart of a University Student's Day")
plt.show()
