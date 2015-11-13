from matplotlib.pylab import figure, axes, pie, title, savefig, clf
import csv
import sys

#To run from command line
#   python pie.py CSV_FileName Name_Of_Grade Minimum_Threshold Maximum_Threshold

# Read CSV to define dictionaries for total students and students that met the threshold within each major
#    totalStudents = {'BACS': 50, 'BSCS': 38, 'BASE': 5, 'BSSE': 10}
#    metStudents = {'BACS': 48, 'BSCS': 33, 'BASE': 3, 'BSSE': 8}
def readCSV(filename):
    total_stu = dict()
    met_stu = dict()
    with open(filename, newline='', encoding='utf-8') as csvfile:
        inputcsv = csv.DictReader(csvfile)
        for row in inputcsv:
            total_stu[row['Major']] = int(row['Total Students'])
            met_stu[row['Major']] = int(row['Met Threshold'])
    return total_stu, met_stu

def createPieCharts(grade, total, met, min_threshold, max_threshold):
    for major, total in total.items():
        # Make a square figure and axes
        figure(1, figsize=(6,6))
        ax = axes([0.1, 0.1, 0.8, 0.8])
        # The slices will be ordered and plotted counter-clockwise.
        labels = 'Met threshold', 'Did not meet threshold'
        fracs = [met[major]/total, (total-met[major])/total]
        # Pop the slice of the pie out for emphasis
        explode=(0.1, 0)
        pie(fracs, explode=explode, labels=labels,
               autopct='%1.1f%%', shadow=True, startangle=90)
        title('%s Students Between %s-%s for Assignment %s' % (major, min_threshold, max_threshold, grade),
                 bbox={'facecolor':'0.8', 'pad':5})
        # Save the figure as a png
        savefig("piechart_%s_%s_%s-%s.png" % (grade, major, min_threshold, max_threshold), bbox_inches="tight")
        clf()

def main():
    #System arguments should be as follows
    #   sys.argv[1] = Filename of CSV generated from range.py
    #   sys.argv[2] = Name of Grade
    #   sys.argv[3] = Minimum Threshold value
    #   sys.argv[4] = Maximum Threshold value
    totalStudents, metStudents = readCSV(sys.argv[1])
    createPieCharts(sys.argv[2], totalStudents, metStudents, sys.argv[3], sys.argv[4])

if __name__ == "__main__":
    main()
