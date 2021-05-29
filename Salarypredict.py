import pandas
db=pandas.read_csv("SalaryData.csv")
x=db['YearsExperience'].values.reshape(30,1)
y=db['Salary']
from sklearn.linear_model import LinearRegression
mind=LinearRegression()
mind.fit(x,y)
print('Weightage is : ')
print(mind.coef_)
print('Constant is : ')
print(mind.intercept_)
print('Salary ')
YearsofExperience=float(input('Enter years of experience :'))
print("Your salary would be : ",mind.predict([[YearsofExperience]]))  
