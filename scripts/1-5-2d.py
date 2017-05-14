import scipy as sp
import matplotlib.pyplot as plt

def error(f, x, y):
    return sp.sum((f(x)-y)**2)

data = sp.genfromtxt("ch01/data/web_traffic.tsv", delimiter="\t")

x = data[:,0]
y = data[:,1]

x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

fp1, residuals, rank, sv, rcond = sp.polyfit(x, y, 1, full=True)
fp2 = sp.polyfit(x, y, 2)


f1 = sp.poly1d(fp1)
f2 = sp.poly1d(fp2)
fx = sp.linspace(0, x[-1], 1000)

print("1d")
print("Model parameters: %s" %fp1)
print(error(f1, x, y))

print("2d")
print("Model parameters: %s" %fp2)
print(error(f2, x, y))

plt.plot(fx, f1(fx))
plt.plot(fx, f2(fx))
plt.legend(["d=%i" %f1.order], loc="upper left")
plt.legend(["d=%i" %f2.order], loc="upper left")
plt.scatter(x, y)
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)],
        ['week %i' %w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()
plt.show()
