#%% 
import pandas as pd
import matplotlib.pyplot as plt
survey = pd.read_csv("clean_class_survey_v2.csv")
# %%
survey["grade"].value_counts()
survey["favorite_subject"].value_counts()
#Split, Apply, Combine(presenting it together)
survey.groupby('grade')["minutes_gaming"].mean() #group by grade, then find the mean of their minutes gaming
# %%
#Group by favorite_subject, average minutes_reading, round the average to 1 decimal place, and sort the results in largest ---> smallest order
fav_subject_reading_avg = (survey.groupby("favorite_subject")
       ["minutes_reading"].mean().round(1).sort_values(ascending=False))
#Entering just seperates the code into different lines
fav_subject_reading_avg
# %%
#Which type of pet owner game the most?
survey["pet"].value_counts()
survey.groupby("pet")["minutes_gaming"].mean().round(1)
# Pandas skips the people who don't have pets AKA we don't see them when using the line above
# %%
#This fixes that
survey["pet"] = survey["pet"].str.title()
survey["pet"] = survey["pet"].fillna("No pet")
survey["pet"].value_counts()

# %%
# Show average +group count side-by-side
survey.groupby("favorite_subject")["minutes_reading"].agg(["mean", "count"]).round(1).sort_values("mean", ascending=False)
# size() will count the rows, count() will count the real values
# %%
plt.bar(fav_subject_reading_avg.index, fav_subject_reading_avg.values, color = "#21AFAAD1")
plt.title("Average Minutes Reading by Favorite Subject")
plt.xlabel("Favorite Subject")
plt.ylabel("Average Minutes Reading")
plt.savefig("Minutes_Reading_For_Fav_Subject.png")

# %%
