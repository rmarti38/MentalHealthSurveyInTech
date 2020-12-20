import pandas as pd

mentalHealthSurvey = pd.read_csv("survey.csv")
#cleaning up gender column
mentalHealthSurvey['Gender'] = mentalHealthSurvey['Gender'].replace(to_replace='^[fF].*', value='F', regex=True)
mentalHealthSurvey['Gender'] = mentalHealthSurvey['Gender'].replace(to_replace='^[mM].*', value='M', regex=True)
print(mentalHealthSurvey['Gender'])

#Are men or women more prone to having or developing mental illness in tech?
