import scipy as sp
import matplotlib.pyplot as plt

def error(f, x, y):
    return sp.sum((f(x)-y)**2)

data = sp.genfromtxt("ch01/data/web_traffic.tsv", delimiter="\t")


x = data[:,0]
y = data[:,1]
x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

inflection = 3.5 * 7 * 24
xa = x[:inflection]
ya = y[:inflection]
xb = x[inflection:]
yb = y[inflection:]


fa = sp.poly1d(sp.polyfit(xa, ya, 1))
fb = sp.poly1d(sp.polyfit(xb, yb, 1))

print(error(fa, xa, ya) + error(fb, xb, yb))

fx = sp.linspace(0, x[-1], 1000)
plt.plot(fx, fa(fx))
plt.plot(fx, fb(fx))
plt.legend(["d=%i" %fa.order], loc="upper left")
plt.legend(["d=%i" %fb.order], loc="upper left")

plt.scatter(x, y)
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)],
        ['week %i' %w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()
plt.show()
