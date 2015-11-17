from argparse import ArgumentParser
from csv import DictReader, DictWriter

# usage: python range.py "filepathtogradebook" "filepathtomajors" "filepathtoresults" "gradebook_studentid" "gradebook_assignment" "major_studentid" "major_name" lowerthresholdinclusive higherthresholdexclusive [--verbose]
def get_arguments():
	parser = ArgumentParser()
	parser.add_argument('gradebook')
	parser.add_argument('majorlist')
	parser.add_argument('range_results')
	parser.add_argument('grade_id')
	parser.add_argument('grade_column')
	parser.add_argument('major_id')
	parser.add_argument('major_column')
	parser.add_argument('lower_threshold', type=float)
	parser.add_argument('higher_threshold', type=float)
	parser.add_argument('-v', '--verbose', action='store_true')
	return parser.parse_args()

def read_in_data(source, id, data, repository, wrapper=lambda a: a):
	with open(source, newline='', encoding='utf-8') as f:
		reader = DictReader(f)
		for row in reader:
			repository[row[id]] = wrapper(row[data])

def main():
	args = get_arguments()
	
	if args.verbose:
		print(args)

	grades = dict()
	majors = dict()
	
	# read in data from gradebook and majorlist
	read_in_data(args.gradebook, args.grade_id, args.grade_column, grades, float)
	read_in_data(args.majorlist, args.major_id, args.major_column, majors)

	# preliminary warning
	if args.verbose and len(grades) != len(majors):
		print('There is a size mismatch between the gradebook and the majors list; however, analysis will do as much as it can.')
	
	# sanity check
	if args.verbose:
		for id in grades:
			if id not in majors:
				print('There is a student in the gradebook who is not on the majors list with the id: ' + id + '.')
				continue
			else:
				print(id + " " + majors[id] + " " + str(grades[id]))
			
	# analysis
	met_threshold = {major: [0, 0] for major in majors.values()} # [number_met_threshold, total_number]
	for id in grades:
		if id in majors:
			met_threshold[majors[id]][1] += 1
			met_threshold[majors[id]][0] += 1 if grades[id] >= args.lower_threshold and grades[id] < args.higher_threshold else 0
	if args.verbose:
		print(met_threshold)
	
	# print to csv
	with open(args.range_results, 'w', newline='', encoding='utf-8') as f:
		headers = ['Major', 'Total Students', 'Met Threshold', 'Percentage']
		writer = DictWriter(f, fieldnames=headers)
		
		writer.writeheader()
		for major in met_threshold:
			writer.writerow({headers[0]: major, headers[1]: met_threshold[major][1], headers[2]: met_threshold[major][0], headers[3]: "{0:f}".format(round(100*met_threshold[major][0]/met_threshold[major][1]))})
	
	if args.verbose:
		print('done')	

if __name__ == "__main__":
	main()