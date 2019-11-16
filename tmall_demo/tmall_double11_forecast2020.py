#author: hanshiqiang365 （微信公众号：韩思工作室）

import matplotlib.pyplot as plt
import numpy as np

x = np.array([year for year in range(2009,2020)])
y = np.array([0.5,9.36,52,191,352,571,912,1207,1682.69,2135,2684])
z1 = np.polyfit(x, y, 3)
p1 = np.poly1d(z1)

yvals=p1(x)
plot1=plt.plot(x, y, '*',label='Actual Sales')
plot2=plt.plot(x, yvals, 'r',label='Fit Sales')
plt.xlabel('Year')
plt.ylabel('Sales (100 million) ')
plt.legend(loc=4) 
plt.title('2009-2019 TMALL 11/11 Sales Fitting Curve - hanshiqiang365')
plt.figure(figsize=(10, 10))
plt.show()

print('Fitting Polynomial:',p1) 
p1 = np.poly1d(z1)
print("-"*40)
print('2020年预测值:',p1(2020)) 
