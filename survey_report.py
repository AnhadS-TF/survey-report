#%%
import pandas as pd
import matplotlib.pyplot as plt

survey = pd.read_csv("class_survey.csv")
#%%
# How many students are in each grade?
plt.figure(figsize=(9,5))
counts = survey["grade"].value_counts()
plt.bar(counts.index, counts.values, color="#7B06DB")
plt.title("How Many Students are in Each Grade?")
plt.xlabel("Grade")
plt.ylabel("Number of Students")
plt.tight_layout()

#this is my thing so it looks good
plt.xlim(left=5)
plt.xlim(right=8)

plt.savefig("chart_one.png", dpi=150)
# %%
#What pets do we Have?
plt.figure(figsize=(9,5))
plt.hist(survey["pet"], bins=5, color="#7B06DB", edgecolor="white")
plt.title("What Pets do we Have?")
plt.xlabel("Pet")
plt.ylabel("Number of Students")

#Also my thing but so it's ez to read
plt.ylim(top=12)

plt.tight_layout()
plt.savefig("chart_two.png", dpi=150)
#%%
print(f"Finding one: 35 students are in 6th grade, while 5 are in 7th.")
print(f"Finding two: 11 students have fish, 9 have hamsters, 5 have cats, 10 don't have a pet, and 5 have a dog.")

#%%
#Does minutes reading affect minutes gaming

plt.figure(figsize=(9,5))
plt.scatter(survey["minutes_reading"], survey["minutes_gaming"], color="#7B06DB", edgecolor="white")
plt.title("Does Our Time Reading Affect Our Time Gaming?")
plt.xlabel("Minutes Reading")
plt.ylabel("Minutes Gaming")
plt.tight_layout()
plt.show()
# %%
print(len(survey))
gamers = survey[survey["minutes_gaming"] > 60]
print(len(gamers))
print(len(survey))
#%%
survey["hours_gaming"] = survey["minutes_gaming"] / 60
survey.head()

survey["screen_vs_book"] = survey["minutes_gaming"] - survey["minutes_reading"] # If positive, they game more than they read. If negative, they read more than they game.

survey.sort_values(["grade", "minutes_reading"], ascending=[True, False])

survey["hours_sleep"].describe()

# %%
