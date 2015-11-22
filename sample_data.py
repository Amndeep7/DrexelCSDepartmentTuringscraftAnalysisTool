import argparse
import csv
import random
import string

def get_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument('gradebook')
	parser.add_argument('majorlist')
	parser.add_argument('sample_size', type=int)
	parser.add_argument('num_majors', type=int)
	parser.add_argument('num_grades', type=int)
	return parser.parse_args()

def generate_sample_data(sample_size, num_majors, num_grades, gradebook, majorlist):
	ids = [random.randrange(10000000, 100000000) for x in range(sample_size)] # student ids are 8 digits long
	major_names = [''.join(random.choice(string.ascii_uppercase) for x in range(random.randrange(3, 7))) for y in range(num_majors)] # major ids are generally between 3 and 6 characters long
	grade_names = [''.join(random.choice(string.ascii_uppercase) for x in range(3)) + str(y+1) for y in range(num_grades)]
	
	majors = {id: random.choice(major_names) for id in ids}
	grades = {id: {name: min(max(0, round(random.gauss(70, 15), 2)), 100) for name in grade_names} for id in ids}
	
	with open(majorlist, 'w', newline='', encoding='utf-8') as f:
		headers = ['Student ID', 'Major']
		writer = csv.DictWriter(f, fieldnames=headers)
		writer.writeheader()
		
		id_keys = ids
		random.shuffle(id_keys)
		for id_key in id_keys:
			writer.writerow({headers[0]: id_key, headers[1]: majors[id_key]})
			
	with open(gradebook, 'w', newline='', encoding='utf-8') as f:
		headers = ['Student ID'] + grade_names
		writer = csv.DictWriter(f, fieldnames=headers)
		writer.writeheader()
		
		id_keys = ids
		random.shuffle(id_keys)
		for id_key in id_keys:
			writer.writerow({**{headers[0]: id_key}, **{grade_name: grades[id_key][grade_name] for grade_name in grade_names}}) # c = {**a, **b} where a, b are dicts results in a dict merging the two (introduced in 3.5)
			
def main():
	args = get_arguments()
	generate_sample_data(args.sample_size, args.num_majors, args.num_grades, args.gradebook, args.majorlist)
	
if __name__ == "__main__":
	main()