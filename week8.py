#%%
import pandas as pd
import matplotlib.pyplot as plt
survey = pd.read_csv('class_survey_v2_clean.csv')

#%%

#create a dataframe called sleep, which stores the data grouped by grade 
# and gets the average hours of sleep per grade rounded to 2 decimals
sleep = survey.groupby("grade")["hours_sleep"].mean().round(2)
# The Misleading
plt.bar(["6th grade", "7th grade"], sleep.values)
plt.ylim(7.4, 7.9)
plt.title("7th Graders Sleep Waay More!")
plt.ylabel(" Average Hours of Sleep")
plt.savefig("Misleading.png")

#%%
# The True 
plt.bar(["6th grade", "7th grade"], sleep.values)
plt.ylim(0.0, 10)
plt.title("Average Sleep is About the Same")
plt.ylabel("Average Hours of Sleep")
plt.savefig("The Unbiased.png")

#%%
sg = (survey.groupby("favorite_subject")["minutes_gaming"]
   .agg(["mean", "count"]).round(1)
   .sort_values("mean", ascending=False)   
      )
plt.bar(sg.index, sg["mean"])
plt.ylim(0, 150)
for i, (mean, n) in enumerate(zip(sg["mean"], sg["count"])):
    plt.text(i, mean +4, f'n={n}', ha = "center")
plt.title("Average Minutes Gaming by Favorite Subject and how many Contributed(40 students)")
plt.xlabel("Subjects")
plt.ylabel("Minutes Gaming")

# %%
