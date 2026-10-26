#%%
import pandas as pd
import matplotlib.pyplot as plt
survey = pd.read_csv("clean_class_survey_v2.csv")
print(survey['pet'].unique())
survey["pet"] = survey["pet"].str.title()
survey["pet"] = survey["pet"].fillna("No pet")
survey.to_csv("clean_class_survey_v2.csv", index=False) 

# %%
