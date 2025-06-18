import matplotlib.pyplot as plt
import matplotlib.dates as dates

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

def axes_format(ax, ship_names: list[str], title: str, xlabel: str, ylabel: str, date: str = "%b %Y"):

    # titles + axis labels
    ax.set(title=title, xlabel=xlabel, ylabel=ylabel)

    # Y-axis
    n = len(ship_names)
    ax.set_yticks(range(n)) #one tick per ship
    ax.set_yticklabels(ship_names)
    ax.invert_yaxis() #invert axis so first docked ship is up top

    # X-axis
    ax.xaxis_date() #treat values as dates
    ax.xaxis.set_major_locator(dates.MonthLocator())
    ax.xaxis.set_major_formatter(dates.DateFormatter(date)) #format as month year
    plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right') #rotate so no overlap

    return ax