from derivative import d_dx
from process_dpt import dpt_to_array
import matplotlib.pyplot as plt
import sys
try:
    file = sys.argv[1]
except IndexError:
    print("No file has been provided!")
    print("Exiting the program...")
    exit()

data = dpt_to_array(file)
print(data[3])

data_deriv = d_dx(data)
print(data_deriv[3])

x_data = []
y_data = []
for i in data:
    x_data.append(i[0])
    y_data.append(i[1])


x_data_deriv = []
y_data_deriv = []
for i in data_deriv:
    x_data_deriv.append(i[0])
    y_data_deriv.append(i[1])

tolerance = 0.0001
for i in range(len(y_data_deriv)):
    if tolerance > y_data_deriv[i] > -tolerance and y_data[i] > 0.02:
        print(f"{x_data_deriv[i]} : {y_data_deriv[i]}")

plt.plot(x_data, y_data)
plt.plot(x_data_deriv, y_data_deriv)
plt.show()
