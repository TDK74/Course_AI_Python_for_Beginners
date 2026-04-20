import matplotlib.pyplot as plt
import pandas as pd


## ------------------------------------------------------ ##
data = pd.read_csv('car_data.csv')

print(data)

## ------------------------------------------------------ ##
print(data[data["Price"] >= 10000])

expensive_cars = data[data['Price'] >= 10000]
print(expensive_cars)

## ------------------------------------------------------ ##
print(data[data["Year"] == 2015])

## ------------------------------------------------------ ##
filtered_data = data[data["Year"] == 2015]
print(filtered_data["Price"].median())

## ------------------------------------------------------ ##
plt.scatter(data["Kilometer"], data["Price"])

plt.title('Car Price vs. Kilometers Driven')
plt.xlabel('Kilometers Driven')
plt.ylabel('Price (in USD)')

plt.show()

## ------------------------------------------------------ ##
plt.scatter(data["Kilometer"], data["Price"], color = 'red')
plt.title('Car Price vs. Kilometers Driven', fontsize = 16)
plt.xlabel('Kilometers Driven')
plt.ylabel('Price (in USD)')

plt.grid(True)

plt.show()

## ------------------------------------------------------ ##
print(data[data["Model"].str.contains("Amaze")])

print('============================================================')

honda_model = data[data["Model"].str.contains("Accord")]
print(honda_model)

## ------------------------------------------------------ ##
median_prices = data.groupby("Year")["Price"].median()

plt.scatter(data["Year"], data["Price"], color = 'orange', label = 'Price')

plt.plot(median_prices.index, median_prices.values, color = 'blue', label = 'Median Price',
        linewidth = 2)

plt.title('Car Price vs. Year', fontsize = 14)
plt.xlabel('Years')
plt.ylabel('Price (in USD)')

plt.grid(True)

plt.legend()

plt.show()

## ------------------------------------------------------ ##
cars_per_year = data['Year'].value_counts()

count_labels = [f'{year} : {count}' for year,
                count in zip(cars_per_year.index, cars_per_year.values)]

percentage_labels = cars_per_year.index

fig, axes = plt.subplots(1, 2, figsize = (12, 6))

axes[0].pie(cars_per_year, labels = count_labels)
axes[0].set_title('Cars Sold Per Year (Counts)')

axes[1].pie(cars_per_year, labels = percentage_labels, autopct = '%1.1f%%')
axes[1].set_title('Cars Sold Per Year (Percentages)')

plt.tight_layout()
plt.show()
