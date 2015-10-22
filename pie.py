from pylab import *

# make a square figure and axes
figure(1, figsize=(6,6))
ax = axes([0.1, 0.1, 0.8, 0.8])

# The slices will be ordered and plotted counter-clockwise.
labels = 'Met threshold', 'Did not meet threshold'
fracs = [17.75, 82.25]
explode=(0.1, 0)

pie(fracs, explode=explode, labels=labels,
                autopct='%1.1f%%', shadow=True, startangle=90)
                # The default startangle is 0, which would start
                # the Frogs slice on the x-axis.  With startangle=90,
                # everything is rotated counter-clockwise by 90 degrees,
                # so the plotting starts on the positive y-axis.

title('BACS Students between 50-75% for A3 Grade', bbox={'facecolor':'0.8', 'pad':5})

savefig("piechart_A3_BACS_50-75.png", bbox_inches="tight")
