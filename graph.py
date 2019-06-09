import matplotlib.pyplot as plt 
import numpy as np 


def graph():
    # -3*(x-30)**2*sin(x) 
    x = np.linspace(0, 15, 200)
    y=(-3)*(x-30)**2*np.sin(x)
    plt.figure()
    plt.plot(x, y)
    plt.show()
if __name__ == "__main__":
    graph()