
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib	import cm


def view_colormap(cmap):
    """Plot a colormap"""
    cmap = plt.cm.get_cmap(cmap)
    colors = cmap(np.arange(cmap.N))
    
    fig, ax = plt.subplots(1, figsize=(6, 2),
                           subplot_kw=dict(xticks=[], yticks=[]))
    ax.imshow([colors], extent=[0, 10, 0, 1])
    plt.show()


top = cm.get_cmap('PiYG', 128)
bottom = cm.get_cmap('Blues',128)
newcolors = np.vstack((top(np.linspace(0.25, 0.5, 128)),
                       bottom(np.linspace(0, 0.5, 128))))
newcmp = ListedColormap(newcolors, name='trns')



view_colormap(newcmp)




