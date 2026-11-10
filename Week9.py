#%%
import pandas as pd
import matplotlib.pyplot as plt

#%%
df = pd.read_csv('clean_class_survey_v2.csv')

#%%
d = df.dropna(subset=['hours_sleep', 'minutes_gaming']) #Only keeps students who answered both
fig, axes = plt.subplots(1, 2, figsize=(10, 4)) #axes[0] = left chart and axes[1] = right chart

#Draw the left panel
axes[0].scatter(d['minutes_gaming'], d['hours_sleep'])
axes[0].set_xlabel('Minutes Gaming')
axes[0].set_ylabel('Hours of Sleep')
axes[0].set_ylim(0,11)
axes[0].set_title('Every Student (37)')

d = d.copy()
d['group'] = (d['minutes_gaming'] > 90).map({True: 'Games 90+ min', False: "Games under 90"})

g = g.reindex(['Games under 90', 'Games 90+ min'])

axes[1].bar(g.index, g['mean'])
axes[1].set_ylim(0,11)
axes[1].set_ylabel('Average hors of sleep')

for i, (mean, n) in enumerate(zip(g['mean'], g['count'])):
    axes[1].text(i, mean + 0.3, f'n={int(n)}', ha='center')

axes[1].axhline(d['hours_sleep'].mean(), color='red', linestyle='--')

fig.suptitle('Do students who game more sleep less? No - not in our class.')
fig.tight_layout()
fig.savefig('gaming_sleep_story.png')

