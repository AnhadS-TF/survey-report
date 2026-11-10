#%%
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('clean_class_survey_v2.csv')

#%%

#create a dataframe called sleep, which stores the data grouped by grade 
# and gets the average hours of sleep per grade rounded to 2 decimals
sleep = df.groupby("grade")["hours_sleep"].mean().round(2)
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
subject_data = df.dropna(subset=['favorite_subject', 'minutes_gaming'])
g = subject_data.groupby('favorite_subject')['minutes_gaming'].agg(['mean', 'count']).round(2)
sg = (df.groupby("favorite_subject")["minutes_gaming"]
   .agg(["mean", "count"]).round(1)
   .sort_values("mean", ascending=False)   
      )
plt.bar(sg.index, sg["mean"])
plt.ylim(0, 160)
for i, (mean, n) in enumerate(zip(sg["mean"], sg["count"])):
    plt.text(i, mean +4, f'n={n}', ha = "center")
plt.title("Average Minutes Gaming by Favorite Subject and how many Contributed(40 students)")
plt.xlabel("Subjects")
plt.ylabel("Minutes Gaming")

# %%
# EXTRA STUFF WE DO TO THIS IN WEEK 10
fig, ax = plt.subplots(figsize = (8, 5))
ax.set_title(" Students who like PE game the most - about 2 hours a day", fontsize = 16)
ax.set_xlabel("Favorite School Subject", fontsize=13)
ax.set_ylim(0,150)
ax.set_ylabel("Average Minutes Gaming per day", fontsize=13)
ax.tick_params(labelsize=12)
#Typical Projector sizes
#Title: 16
#Labels: 13
#Tick Labels: 12 
#Caption: 10

for i, (mean, n) in enumerate(zip(g['mean'], g['count'])):
    label = f'{int(round(mean))} min'
    label = label + f'\n({n} students)'
    #pressing backslash ABOVE gives us a new line below that string IN WHICH we put the other stuff we type after that string. 
    ax.text(i,mean + 5, label, ha="center", fontsize=11)
# HIGHLIGHT one bar
colors = []
for subject in g.index:
    if subject == 'PE':
        colors.append("#00EEFF")
    else:
        colors.append("#FF0000")
ax.bar(g.index, g['mean'], color=colors)    

fig.tight_layout()
fig.subplots_adjust(bottom=0.22)
fig.text(0.5, 0.06, 'Only 5 students picked PE, so this gap could change a lot with one more answer.', ha='center', fontsize=10)
fig.savefig('one_pager.png', dpi=150)