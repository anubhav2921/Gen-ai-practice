import matplotlib.pyplot as plt
countries = ['India', 'China', 'USA', 'Brazil', 'Germany'] 
gdp       = [3.75, 17.7, 25.5, 2.1, 4.3] 
 
plt.figure(figsize=(8, 5)) 
plt.barh(countries, gdp, color='teal', edgecolor='black') 
plt.xlabel('GDP (Trillion USD)') 
plt.title('GDP by Country') 
plt.tight_layout() 
plt.show() 