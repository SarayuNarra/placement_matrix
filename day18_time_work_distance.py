# Day 18: Aptitude Practice
# Topics: Time & Work and Time & Distance
# 10 Questions with Answers

print("Day 18: Time & Work + Time & Distance Practice\n")

# ---------------- TIME & WORK ----------------

# Q1: A can complete a work in 10 days. What is A's 1 day work?
print("Q1: A's 1 day work =", 1/10)

# Q2: A can do a work in 10 days and B in 20 days. How long together?
work_per_day = (1/10) + (1/20)
print("Q2: Together time =", 1 / work_per_day, "days")

# Q3: 5 men can do a work in 12 days. How many days for 10 men?
total_work = 5 * 12
print("Q3: Days for 10 men =", total_work / 10)

# Q4: A and B earn ₹600. If their efficiency ratio is 2:1, find A's share.
print("Q4: A's wage =", (2/3) * 600)

# Q5: A is twice as efficient as B. If A takes 10 days, B takes:
print("Q5: B's time =", 10 * 2, "days")


# ---------------- TIME & DISTANCE ----------------

# Q6: A car travels at 40 km/hr for 3 hours. Find distance.
print("Q6: Distance =", 40 * 3, "km")

# Q7: Convert 54 km/hr into m/s.
print("Q7: Speed =", 54 * 5 / 18, "m/s")

# Q8: Two trains move towards each other at 50 km/hr and 60 km/hr.
print("Q8: Relative speed =", 50 + 60, "km/hr")

# Q9: A train 100 m long passes a pole in 10 seconds. Find speed.
print("Q9: Speed =", 100 / 10, "m/s")

# Q10: A person goes at 30 km/hr and returns at 60 km/hr. Find average speed.
avg_speed = (2 * 30 * 60) / (30 + 60)
print("Q10: Average speed =", avg_speed, "km/hr")
