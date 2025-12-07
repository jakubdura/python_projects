import pandas as pd
import statsmodels.api as sm

df = pd.DataFrame({
    'hours': [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14],
    'exams': [70, 73, 76, 80, 78, 85, 88, 90, 92, 94, 96, 100],
    'score': [79, 80, 76, 83, 82, 87, 84, 90, 93, 89, 91, 76]
})

y = df['score']
x = df[['hours', 'exams']]
x = sm.add_constant(x)

model = sm.OLS(y, x).fit()
print(model.summary())
