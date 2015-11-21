from random import choice, randint
import csv

def generate_sample_data():
	id_creator = [] 
	major_creator = ["BACS", "BSCS", "BASE", "BSSE", "XYZ"]
	c = csv.writer(open("major.csv", "wb")) #create an object for writing
	c.writerow(["Student ID", "Major"]) #write the CSV file
	c1 = csv.writer(open("gradebook.csv", "wb"))
	c1.writerow(["Student ID", "A1 Grade", "A2 Grade", "A3 Grade"])

	for x in range(50):
		for i in range(0,7):
			id_creator.append(randint(0,9))
		student_id = ''.join(str(e) for e in id_creator)
		
		major = choice(major_creator)
		grade1 = randint(50, 100)
		grade2 = randint(50, 100)
		grade3 = randint(50, 100)
		id_creator = []
		c.writerow([student_id, major])
		c1.writerow([student_id, grade1, grade2, grade3])