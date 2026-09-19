import numpy as np

print("NUMPY DATA EXPLORER")
print("===================")

numbers = np.array([10, 20, 30, 40, 50])

print("\nOur array:")
print(numbers)

print("\nFirst number:")
print(numbers[0])

print("\nThird number:")
print(numbers[2])

print("\nFirst three numbers:")
print(numbers[0:3])

print("\nArray multiplied by 2:")
print(numbers * 2)
print("\nArray divided by 10:")
print(numbers / 10)
print("\nArray plus 5:")
print(numbers + 5)
print("\nArray minus 3:")
print(numbers - 3)

print("\nMean of the array:")
print(np.mean(numbers))
print("\nStandard deviation of the array:")
print(np.std(numbers))
print("\nMinimum value in the array:")
print(np.min(numbers))
print("\nMaximum value in the array:")
print(np.max(numbers))
print("\nSum of the array:")
print(np.sum(numbers))

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\n2D array:")
print(data)

print("\nShape of the 2D array:")
print(data.shape)

print("\nValue at row 1, column 2:")
print(data[1, 2])

numbers2 = np.array([10, 20, 30, 40, 50, 60])
reshaped = numbers2.reshape(2, 3)
print("\nReshaped array (2 rows, 3 columns):")
print(reshaped)

prices = np.array([100, 200, 300,])
tax = 10
final_prices = prices + tax
print("\nOriginal prices:")
print(prices)
print("\nPrices after tax:")
print(final_prices)

np.save('numbers.npy', numbers2)
print("\nArrays saved successfully.")

loaded_numbers = np.load('numbers.npy')
print("\nLoaded array:")
print(loaded_numbers)

import timeit
size =1_000_000
python_list = list(range(size))
numpy_array = np.arange(size)
list_time= timeit.timeit(lambda: [x * 2 for x in python_list], number=10)
numpy_time = timeit.timeit(lambda: numpy_array * 2, number=10)

print("\nPerfomance Comparison:")
print("Python list time:", list_time)
print("NumPy array time:", numpy_time)

if numpy_time < list_time:
    print("NumPy is faster in this test.")
else:
    print("Python list is faster in this test.")