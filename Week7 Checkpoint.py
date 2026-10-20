#%% 
import pandas as pd
import matplotlib.pyplot as plt
survey = pd.read_csv("clean_class_survey_v2.csv")

 #%%
survey["grade"].value_counts()
# 24 students are in grade 6 and 16 students are in grade 7.

#%%
survey.groupby("grade")["hours_sleep"].mean().round(1).sort_values(ascending=False)
# Grade 6 has an average of 49.3 hours of sleep while grade 7 has an average of 32.0 hours of sleep.

#%%
avg = (survey.groupby("favorite_subject")["minutes_gaming"].mean().round(1).sort_values(ascending=False))
plt.bar(avg.index, avg.values, color="#AA00FF74")
plt.xlabel("Favorite Subjects")
plt.ylabel("Minutes Gaming")
plt.title("Minutes Gaming for Our Favorite Subjects")
plt.savefig("checkpoint_chart.png")

# %%
avg
# Fans of P.E. game the most, with  