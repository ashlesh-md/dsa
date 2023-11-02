import matplotlib.pyplot as plt

sequence = [0, 2 ,3 ,4 , 5 ,4 , 3, 2, 1]
x = list(range(len(sequence)))

plt.plot(x, sequence)
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('0 1 0 1 0 1 0 1 0 1 Sequence')
plt.grid(True)
plt.show()
