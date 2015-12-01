## DrexelCSDepartmentAnalysisTool

#Authors:

Amndeep Singh Mann - asm357@drexel.edu
	
Mansoor Siddiqui - mis43@drexel.edu
	
Ryan Efendy - re88@drexel.edu

#Purpose:

Create a tool to automate data analysis of Dr. Mongan's student data project

#Dependencies:

- Python3
- matplotlib

#Usage

To generate sample data:

python sample_data.py "filepathtogradebook" "filepathtomajorslist" sample_data_size number_of_different_major_types number_of_different_assignments

=>

python sample_data.py gradebook.csv major.csv 50 4 3

To analyze data:

python range.py "filepathtogradebook" "filepathtomajorslist" "filepathtoresults" "gradebook_studentid" "gradebook_assignment" "major_studentid" "major_name" lowerthresholdinclusive higherthresholdexclusive [--verbose]

=>

python range.py gradebook.csv major.csv results.csv "Student ID" L2 "Student ID" BSCS 70 100.1  --verbose

To create piecharts representing the data:

python pie.py "filepathtoresults" "gradebook_assignment" lowerthresholdinclusive higherthresholdexclusive

=>

python pie.py results.csv L2 70 100.1

To combine the analysis and piechart functionality into one script:

python main.py "filepathtogradebook" "filepathtomajorslist" "filepathtoresults" "gradebook_studentid" "gradebook_assignment" "major_studentid" "major_name" lowerthresholdinclusive higherthresholdexclusive

=>

python main.py gradebook.csv major.csv results.csv "Student ID" L2 "Student ID" BSCS 70 100.1