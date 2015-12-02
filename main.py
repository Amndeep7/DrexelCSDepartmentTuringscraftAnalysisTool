import argparse
import subprocess

# usage: python main.py "filepathtogradebook" "filepathtomajors" "filepathtoresults" "gradebook_studentid" "gradebook_assignment" "major_studentid" "major_name" lowerthresholdinclusive higherthresholdexclusive
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
	
# runs both range.py and pie.py so as to simplify process for user
def main():
	args = get_arguments()
	subprocess.run(["python", "range.py", args.gradebook, args.majorlist, args.range_results, args.grade_id, args.grade_column, args.major_id, args.major_column, str(args.lower_threshold), str(args.higher_threshold)])
	subprocess.run(["python", "pie.py", args.range_results, args.grade_column, str(args.lower_threshold), str(args.higher_threshold)])

if __name__ == "__main__":
	main()