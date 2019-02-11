import math
def normal_pdf(x, mu=0, sigma=1):   

    pie = math.pi
    sigmasquare = math.pow(sigma, 2)

    a = 1 / (math.sqrt(2*pie*sigmasquare))
    exponent = -((math.pow((x - mu), 2)) / (2*sigmasquare))
    b = math.exp(exponent)

    return  a * b
    # TODO
    # hits: math.exp

from matplotlib import pyplot as plt
xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='mu=0,sigma=1')
plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '-', label='mu=0,sigma=2')
plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], '-', label='mu=0,sigma=0.5')
plt.plot(xs, [normal_pdf(x, sigma=-1) for x in xs], '-', label='mu=0,sigma=-1')
plt.legend()
plt.show()