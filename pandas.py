import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employee.csv")

print(df[["Name", "Department", "Salary"]])

avg = df.groupby("Department")["Salary"].mean()
print("\nAverage Salary:")
print(avg)

avg.plot(kind="bar")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.show()
