from matplotlib.pylab import figure, axes, pie, title, savefig, clf
import csv
import sys

#To run from command line
#   python pie.py CSV_FileName Name_Of_Grade Minimum_Threshold Maximum_Threshold

# Read CSV to define dictionaries for total students and students that met the threshold within each major
def read_csv(filename):
    total_students = dict()
    met_students = dict()
    with open(filename, newline='', encoding='utf-8') as csvfile:
        inputcsv = csv.DictReader(csvfile)
        for row in inputcsv:
            total_students[row['Major']] = int(row['Total Students'])
            met_students[row['Major']] = int(row['Met Threshold'])
    return total_students, met_students

def create_piecharts(grade, total_students, met_students, min_threshold, max_threshold):
    for major, total in total_students.items():
        # Make a square figure and axes
        figure(1, figsize=(6,6))
        ax = axes([0.1, 0.1, 0.8, 0.8])
        # The slices will be ordered and plotted counter-clockwise.
        labels = 'Met threshold', 'Did not meet threshold'
        fracs = [met_students[major]/total, (total-met_students[major])/total]
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
    total_students, met_students = read_csv(sys.argv[1])
    create_piecharts(sys.argv[2], total_students, met_students, sys.argv[3], sys.argv[4])

if __name__ == "__main__":
    main()
