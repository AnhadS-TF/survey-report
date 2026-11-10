#%%
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("clean_class_survey_v2.csv")
# %%
d = df.dropna(subset=['hours_sleep', 'minutes_gaming']) #Only keeps students who answered both
fig, axes = plt.subplots(1, 2, figsize=(10, 4)) #axes[0] = left chart and axes[1] = right chart

#Left panel time!
axes[0].scatter(d['minutes_gaming'], d['minutes_reading'])
axes[0].set_xlabel('Minutes Gaming')
axes[0].set_ylabel('Minutes Reading')
axes[0].set_ylim(0,12)
axes[0].set_title('Every Student that answered both(37)')


# Righty now

g = (d.groupby('minutes_gaming')['hours_sleep'].agg(['mean', 'count']).round(2))


axes[1].bar(g.index, g['mean'])
axes[1].set_ylim(0,11)
axes[1].set_ylabel('Average hours of sleep')

for i, (mean, n) in enumerate(zip(g['mean'], g['count'])):
    axes[1].text(i, mean + 0.3, f'n={int(n)}', ha='center')

axes[1].axhline(d['hours_sleep'].mean(), color='red', linestyle='--')