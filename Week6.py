 #%%
import pandas as pd
import matplotlib.pyplot as plt
# pd and plt are variables that can be changed, but only if you change every where it says pd or plt to that new thing, say theroy
survey = pd.read_csv("class_survey_v2.csv")

#How many missing values r there?
print (survey.isna().sum()) # isna = "not applicable"
# pandas treats "None" as a missing value
#It also treats NaN, NA, N/A, etc as a missing value
#%%
# Next we will fix the data inconsistency
print(survey['grade'].unique()) #how many unique values are in the grade column? #Also the 7th means there are 7th-s, not just 1 7th
# %%
grade_map = {'6':6, '6th':6, 'six':6, '7':7, '7th':7, 'seven':7}# There is no "seven" but we do that to prepare ahead for future data that gets added
#Now we actually change the values in the .csv
# %%
#strings r a collection of charecters, like "That's just a theory" 
survey['grade'] = (survey['grade'].astype(str).str.strip().map(grade_map))
#we should get the current grade, remove spaces around it, and then map it to grade_map we created above
# %%
#checking if it worked
print(survey)
#It did
# %%
#Fixing the duplicate
survey = survey.drop_duplicates()
print(survey)
# %%
#check for impossibilities
print(survey['hours_sleep'].describe())
survey.loc[survey['hours_sleep'] > 24, 'hours_sleep'] = pd.NA
#The line above locates the records where sleep > 24 hrs, and updates the sleep column to NA. pd.NA ->specifies
# %%
#Fixing fav subject : math, MATH, P.E, pe, etc
print(survey['favorite_subject'].unique())
survey['favorite_subject'] = survey['favorite_subject'].str.strip().str.title()#prints as a title would -1st lettter capital and everything else lowercase
#PE got messed up cuz we forced eberything to be a title, while PE should have been left as is
survey['favorite_subject'] = survey['favorite_subject'].replace({'P.E.': 'PE', 'Pe': 'PE'})
# %%
#Challenge: Make all the NaN-s in pets column to blank, like ""
survey.loc[survey['pet'].isna(), 'pet'] = "None"
print(survey)


# %%
print(survey["pet"].unique()) 
survey['pet'] = survey['pet'].str.strip().str.title()
survey['pet'] = survey['pet'].replace({'BIRD': 'Bird', 'HAMSTER': 'Hamster', 'DOG': 'Dog', 'CAT': 'Cat', 'FISH': 'Fish'})

# %%
print(survey['hours_sleep'].unique())
survey['hours_sleep'] = survey['hours_sleep'].astype(str).str.strip().str.title()
survey['hours_sleep'] = survey['hours_sleep'].str.replace({'8.': '8', '6.': '6', 'nan': '0', '99.': 'Undefined'})
# %%
survey.to_csv("clean_class_survey_v2.csv", index=False) 
