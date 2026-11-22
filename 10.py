
import matplotlib.pyplot as plt

# 1. Line Plot
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 120, 180, 200]

plt.plot(months, sales, color='blue', marker='o')
plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

# 2. Scatter Plot
height = [150, 155, 160, 165, 170]
weight = [45, 50, 55, 60, 65]

plt.scatter(height, weight, color='red')
plt.title("Height vs Weight")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.show()

# 3. Box Plot
marks = [35, 45, 55, 65, 70, 75, 80, 85, 90]

plt.boxplot(marks)
plt.title("Students Marks")
plt.ylabel("Marks")
plt.show()

# 4. Bar Chart
students = ["A", "B", "C", "D"]
marks = [85, 70, 90, 75]

plt.bar(students, marks, color='green')
plt.title("Student Performance")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 5. Pie Chart
activities = ["Study", "Sleep", "Games", "Other"]
hours = [8, 8, 4, 4]

plt.pie(hours, labels=activities, autopct='%1.1f%%')
plt.title("Daily Activities")
plt.show()

