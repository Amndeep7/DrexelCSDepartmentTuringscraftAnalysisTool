import argparse
import csv

def get_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument('gradebook')
	parser.add_argument('majorlist')
	parser.add_argument('range_results')
	parser.add_argument('grade_id')
	parser.add_argument('grade_column')
	parser.add_argument('major_id')
	parser.add_argument('major_column')
	parser.add_argument('lower_threshold', type=float)
	parser.add_argument('higher_threshold', type=float)
	return parser.parse_args()

# usage: python range.py "filepathtogradebook" "filepathtomajors" "assignmentcolumntitle" lowerthresholdinclusive higherthresholdinclusive
def main():
	args = get_arguments()

	grades = dict()
	majors = dict()
	
	with open(args.gradebook, newline='', encoding='utf-8') as f:
		reader = csv.DictReader(f)
		for row in reader:
			grades[row[args.grade_id]] = float(row[args.grade_column])
			
	with open(args.majorlist, newline='', encoding='utf-8') as f:
		reader = csv.DictReader(f)
		for row in reader:
			majors[row[args.major_id]] = row[args.major_column]
			
	if len(grades) != len(majors):
		print('There is a size mismatch between the gradebook and the majors list.')
		
	for id in grades:
		if id not in majors:
			print('There is a student in the gradebook who is not on the majors list.')
			continue
		else:
			print(id + " " + majors[id] + " " + str(grades[id]))
			
	met_threshold = {major: [0, 0] for major in majors.values()}
	for id in grades:
		if id in majors:
			met_threshold[majors[id]][1] += 1
			met_threshold[majors[id]][0] += 1 if grades[id] >= args.lower_threshold and grades[id] < args.higher_threshold else 0
	print(met_threshold)
	

if __name__ == "__main__":
	main()