import scipy as sp
import matplotlib.pyplot as plt

def error(f, x, y):
    return sp.sum((f(x)-y)**2)

data = sp.genfromtxt("ch01/data/web_traffic.tsv", delimiter="\t")


x = data[:,0]
y = data[:,1]
x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

inflection = int(3.5 * 7 * 24)
xa = x[:inflection]
ya = y[:inflection]
xb = x[inflection:]
yb = y[inflection:]

frac = 0.3
split_idx = int(frac * len(xb))
shuffled = sp.random.permutation(list(range(len(xb))))
test = sorted(shuffled[:split_idx])
train = sorted(shuffled[split_idx:])

fbt1   = sp.poly1d(sp.polyfit(xb[train], yb[train], 1))
fbt2   = sp.poly1d(sp.polyfit(xb[train], yb[train], 2))
fbt3   = sp.poly1d(sp.polyfit(xb[train], yb[train], 3))
fbt10  = sp.poly1d(sp.polyfit(xb[train], yb[train], 10))
fbt100 = sp.poly1d(sp.polyfit(xb[train], yb[train], 100))

for f in [fbt1, fbt2, fbt3, fbt10, fbt100]:
    print("Error d=%i: %f" % (f.order, error(f, xb[test], yb[test])))

print(fbt2)
print(fbt2-100000)

from scipy.optimize import fsolve
reached_max = fsolve(fbt2-100000, 800) / (7*24)
print(reached_max)
print("100,000 hits/hour expected at week %f" % reached_max[0])
