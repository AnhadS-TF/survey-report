#%%
import pandas as pd
import matplotlib.pyplot as plt
survey = pd.read_csv("clean_class_survey_v2.csv")
# I'm checking to see the differences in my clean csv and the TF clean csv
# Ok so i did it, BUT it bugged out cuz i changed some names and i deleted the code without thinking and i can't get it back. :(

# %%
avg = (survey.groupby("favorite_subject")["minutes_gaming"].agg(["mean", "count"]).round(1).sort_values("mean",ascending=False))
plt.bar(avg.index, avg["mean"], color="#AA00FF74")
plt.xlabel("Favorite Subjects")
plt.ylabel("Minutes Gaming")
plt.title("Average Minutes Gaming for Our Favorite Subjects")
plt.savefig("checkpoint_chart_hw_honest.png")


for i, (mean, n) in enumerate(zip(avg["mean"], avg["count"])):
    plt.text(i, mean +4, f'n={n}', ha = "center")
# error above
print(" So the first chart didn't mention that it was average minutes reading and it doesn't say how many people contrubuted to each subject. I changed the title and made code. Maybe. It might be that it's total minutes reading.")
plt.tight_layout()