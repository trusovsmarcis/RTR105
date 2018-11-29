from numpy import sin, linspace
from matplotlib import pyplot as plt
def mana_funkcija(x):
    return sin(x)

x = linspace(0,4,11)
#print(vars())
y = mana_funkcija(x)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Funkcija un tas atvasinajumi')
plt.plot(x,y)
plt.plot(x,y,'ro')
plt.legend(['funkcija ar starpvertibas', 'funkcijas dazas vertibas'])
#plt.show()
# atvasinajuma aprekins, izmantojot funkcijas aprekinu
N = len(x)
delta_x = x[1] - x[0]
derivative = []
#print(derivative)
for i in range(N):
    temp = (mana_funkcija(x[i] + delta_x) - mana_funkcija(x[i])) / delta_x
    derivative.append(temp)
    #print(derivative)

plt.plot(x,derivative)
plt.plot(x,derivative,'go')
legend = []
legend.append('funkcija ar starpvertibam')
legend.append('funkcijas dazas vertibas')
legend.append('atvasinajums ar starpvertiba')
legend.append('atvasinajums dazas vertibas')

#plt.legend(legend)
#plt.show()

#atvasinajums_caur_massivu = []
derivative_through_array = []
for i in range(N-1):
    temp = (y[i+1] - y[i]) / (x[i+1] - x[i])
    derivative_through_array.append(temp)

plt.plot(x[0:N-1],derivative_through_array)
plt.plot(x[0:N-1],derivative_through_array,'bo')

legend.append('atvasinajums ar starpvertibam (aprekins, izmantojot masiva vertibas')
legend.append('atvasinajuma dazas vertibas (aprekins, izmantojot masiva vertibas)')

plt.legend(legend)
plt.show()

