from matplotlib.pylab import figure, axes, pie, title, savefig, clf

# Define dictionaries for total students and students that met the threshold within each major
totalStudents = {'BACS': 50, 'BSCS': 38, 'BASE': 5, 'BSSE': 10}
metStudents = {'BACS': 48, 'BSCS': 33, 'BASE': 3, 'BSSE': 8}

# Function that creates all pie charts
def createPieCharts(grade, total, met, minThreshold, maxThreshold):
    # Run through each major in the dictionary
    for major, total in total.items():
        # Make a square figure and axes
        figure(1, figsize=(6,6))
        ax = axes([0.1, 0.1, 0.8, 0.8])
        # The slices will be ordered and plotted counter-clockwise.
        # Set labels, and calculate percentage values
        labels = 'Met threshold', 'Did not meet threshold'
        fracs = [met[major]/total, (total-met[major])/total]
        # Pop the slice of the pie out for emphasis
        explode=(0.1, 0)
        # Create the chart
        pie(fracs, explode=explode, labels=labels,
               autopct='%1.1f%%', shadow=True, startangle=90)
        # Set the title
        title('%s Students Between %s-%s for Assignment %s' % (major, minThreshold, maxThreshold, grade),
                 bbox={'facecolor':'0.8', 'pad':5})
        # Save the figure as a png
        savefig("piechart_%s_%s_%s-%s.png" % (grade, major, minThreshold, maxThreshold), bbox_inches="tight")
        clf()

def main():
    args = read_in_args()
    # createPieCharts("A2", totalStudents, metStudents, 80, 100)

if name == "main":
    main()
