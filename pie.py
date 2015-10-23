from pylab import *

totalStudents = {'BACS': 50, 'BSCS': 38, 'BASE': 5, 'BSSE': 10}
metStudents = {'BACS': 48, 'BSCS': 33, 'BASE': 3, 'BSSE': 8}

def createPieCharts(grade, total, met, minThreshold, maxThreshold):
    for major, total in total.items():
        # make a square figure and axes
        figure(1, figsize=(6,6))
        ax = axes([0.1, 0.1, 0.8, 0.8])
        # The slices will be ordered and plotted counter-clockwise.
        labels = 'Met threshold', 'Did not meet threshold'
        fracs = [met[major]/total, (total-met[major])/total]
        explode=(0.1, 0)
        pie(fracs, explode=explode, labels=labels,
               autopct='%1.1f%%', shadow=True, startangle=90)
        title('%s Students Between %s-%s for Assignment %s' % (major, minThreshold, maxThreshold, grade),
                 bbox={'facecolor':'0.8', 'pad':5})
        savefig("piechart_%s_%s_%s-%s.png" % (grade, major, minThreshold, maxThreshold), bbox_inches="tight")
        clf()

createPieCharts("A2", totalStudents, metStudents, 80, 100)
