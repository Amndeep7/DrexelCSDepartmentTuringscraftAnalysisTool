import argparse
import csv

# usage: python check.py "filepathtobblearnroster" "filepathtoturingscraftdata" "filepathtoproblemslist" "filepathtoresults" "roster_studentid" "turingscraft_studentid" "problems_id" [-s "sectionid" sectionnumber]
def get_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument('bblearn')
	parser.add_argument('turingscraft')
	parser.add_argument('problems')
	parser.add_argument('check_results')
	parser.add_argument('bblearn_id')
	parser.add_argument('turingscraft_id')
	parser.add_argument('problems_id')
	parser.add_argument('-s', '--section', nargs=2)
	return parser.parse_args()

# conditional = [id, value] or None
def read_in_data_to_list(source, id, repository, conditional=None):
	with open(source, newline='', encoding='utf-8') as f:
		reader = csv.DictReader(f)
		for row in reader:
			if conditional:
				if row[conditional[0]] == conditional[1]:
					repository.append(row[id])
			else:
				repository.append(row[id])

def read_in_data_to_dictionary(source, id, data, repository):
	with open(source, newline='', encoding='utf-8') as f:
		reader = csv.DictReader(f)
		for row in reader:
			repository[row[id]] = list()
			for datum in data:
				repository[row[id]].append(row[datum])

def identify_headers(source, partials):
	with open(source, newline='', encoding='utf-8') as f:
		line = f.readline().split(',')
		conversion = list()
		for header in line:
			convert = header.split('-')
			if len(convert) == 2:
				convert = convert[1]
			else:
				convert = convert[0]
			if convert in partials:
				conversion.append(header)
		return conversion

def main():
	args = get_arguments()

	names = list()
	problems = list()
	checks = dict()
	
	# read in data from the roster, the list of problems, and the turingscraft data
	read_in_data_to_list(args.bblearn, args.bblearn_id, names, args.section)
	names = list(map(lambda n: n+"@drexel.edu", names))
	read_in_data_to_list(args.problems, args.problems_id, problems)
	read_in_data_to_dictionary(args.turingscraft, args.turingscraft_id, identify_headers(args.turingscraft, problems), checks)
	
	# print to csv
	with open(args.check_results, 'w', newline='', encoding='utf-8') as f:
		headers = ['Email'] + problems + ['Total Completed', 'Percentage Completed']
		writer = csv.DictWriter(f, fieldnames=headers)
		
		writer.writeheader()
		for name in names:
			total = checks[name].count('c')
			values = [name] + checks[name] + [total, total/len(checks[name])]
			writer.writerow(dict(zip(headers, values)))

if __name__ == "__main__":
	main()
