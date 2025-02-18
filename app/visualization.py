import matplotlib.pyplot as plt
import numpy as np
import sqlite3

conn = sqlite3.connect("database.sqlite")
c = conn.cursor()
c.execute("SELECT timestamp, HRV FROM stress_data")
data = c.fetchall()
conn.close()

timestamps = [x[0] for x in data]
stress_values = [x[1] for x in data]

z = np.polyfit(range(len(stress_values)), stress_values, 1)
p = np.poly1d(z)

plt.scatter(range(len(stress_values)), stress_values, label="Stress Levels")
plt.plot(range(len(stress_values)), p(range(len(stress_values))), color="red", label="Trend Line")
plt.xlabel("Time")
plt.ylabel("Stress Level")
plt.legend()
plt.show()
