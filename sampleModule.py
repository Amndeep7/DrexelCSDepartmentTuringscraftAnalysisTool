from random import randint
import random
import csv

def main():
	sampleData()

def sampleData():
	idCreator = []
	majorCreator = ["BACS", "BSCS", "BASE", "BSSE", "XYZ"]
	c = csv.writer(open("major.csv", "wb"))
	c.writerow(["Student ID","Major"])
	c1 = csv.writer(open("gradebook.csv", "wb"))
	c1.writerow(["Student ID", "A1 Grade", "A2 Grade", "A3 Grade"])

	for x in range(50):
		for i in range(0,7):
			idCreator.append(randint(0,9))
		studentId = ''.join(str(e) for e in idCreator)
		
		major = random.choice(majorCreator)
		grade1 = random.randint(50, 100)
		grade2 = random.randint(50, 100)
		grade3 = random.randint(50, 100)
		#print studentId + " " + major
		#print grade
		idCreator = []
		c.writerow([studentId,major])
		c1.writerow([studentId,grade1,grade2,grade3])

if __name__ == "__main__":
    main()