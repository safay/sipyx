import numpy as np
import matplotlib.pyplot as plt
from cStringIO import StringIO
from flaskapp import send_file

def plot_1():
    x = np.linspace(0, 1, 500)
    y = np.sin(4 * np.pi * x) * np.exp(-5 * x)
    fig, ax = plt.subplots()
    ax.fill(x, y, zorder=10)
    ax.grid(True, zorder=5)
    image = StringIO()
    plt.savefig(image)
    plt.close()
    image.seek(0)
    return send_file(image, mimetype='image/png')


def endpoint1(aparam='default', param2='whatever'):
    return "hello world! the parameters are set to: {}, {}".format(aparam, param2)

