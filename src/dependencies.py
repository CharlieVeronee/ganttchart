import matplotlib.pyplot as plt
import pandas as pd

#show dependency where ship docking overlaps and draw arrow between the bars
def draw_docking_overlap(ax, df):

    arrow_font = dict(arrowstyle="->", lw=1, color="black", alpha=0.8)

    starts = df["Docking Start Date"]
    ends   = df["Docking End Date"]
    n = len(df)

    for i in range(n):
        for j in range(i + 1, n): #loop through all combinations
            si, ei = starts.iat[i], ends.iat[i] #iat faster than iloc
            sj, ej = starts.iat[j], ends.iat[j]
            if si < ej and sj < ei: #if overlap

                # midpoint of the overlapping interval
                overlap_start = max(si, sj)
                overlap_end = min(ei, ej)
                mid_pt = overlap_start + (overlap_end - overlap_start) / 2

                y_i = i -.2 #-.2 for aesthetic reasons
                y_j = j -.2

                ax.annotate(
                    "", #empty string
                    xy=(mid_pt, y_j), #head of arriw
                    xytext=(mid_pt, y_i), #start of arrow
                    arrowprops=arrow_font,
                    annotation_clip=False #arrows can exist beyond boundaries
                )
