# DrexelCSDepartmentAnalysisTool

##Authors:

Amndeep Singh Mann - asm357@drexel.edu
	
##Purpose:

Create a tool to read in CSV files holding a roster of students from BBLearn, a TuringsCraft roster, and a list of TuringsCraft problem ids so as to verify if the student has successfully done the problems specified.

##Dependencies:

- Python (compatible with 3.5 on Windows 10 - other versions of Python and operating systems untested)

##Usage

python check.py "filepathtobblearnroster" "filepathtoturingscraftdata" "filepathtoproblemslist" "filepathtoresults" "roster_studentid" "turingscraft_studentid" "problems_id" [-s "sectionid" sectionnumber]

=>

python.exe .\check.py ..\roster-all-2016-01-27-15-12-34.csv ..\turingscraft-2016-01-27.csv ..\problems-pl2.csv ..\results-65-pl2.csv Username Email Problems -s "Lab Section [Total Pts: 70] |989531" 65
