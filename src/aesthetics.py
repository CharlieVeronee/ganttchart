import matplotlib.pyplot as plt

#Return list of colors evenly spaced for graph
def colormap(df, colomap_name='tab10'):
    ships = df['Ship Name'].tolist()
    n = len(ships)
    cmap = plt.get_cmap(colomap_name) #chose the colormap from matplot
    
    samples = [
        cmap(i / (n - 1) if n > 1 else 0.5)
        for i in range(n)
    ]
    return dict(zip(ships, samples))