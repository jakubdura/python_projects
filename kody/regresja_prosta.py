import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Dane
df = pd.DataFrame({
    'hours': [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14],
    'score': [64, 66, 70, 73, 81, 82, 83, 85, 86, 88, 90, 91]
})

print(df.head())

# Scatterplot
plt.scatter(df.hours, df.score)
plt.title("Hours studied vs Exam Score")
plt.xlabel("Hours")
plt.ylabel("Score")
plt.show()

# Boxplot
df.boxplot(column=['score'])
plt.show()

# Regresja liniowa
y = df['score']
x = df[['hours']]
x = sm.add_constant(x)

model = sm.OLS(y, x).fit()
print(model.summary())

# Residual plot
fig = plt.figure(figsize=(12, 8))
sm.graphics.plot_regress_exog(model, 'hours', fig=fig)
plt.show()

# QQ plot
res = model.resid
sm.qqplot(res, fit=True, line='45')
plt.show()
