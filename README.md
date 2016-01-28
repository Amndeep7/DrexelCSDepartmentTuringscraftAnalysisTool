# DrexelCSDepartmentAnalysisTool

##Author:

Amndeep Singh Mann - asm357@drexel.edu
	
##Purpose:

Create a tool to read in CSV files holding a roster of students from BBLearn, a TuringsCraft roster, and a list of TuringsCraft problem ids so as to verify if the student has successfully done the problems specified.

##Dependencies:

- Python (compatible with 3.5 on Windows 10 - other versions of Python and operating systems untested)
- Blackboard Learn (BBLearn) roster output of a format compatible with that produced on 1/27/16
- Turingscraft roster output of a format compatible with that produced on 1/27/16

##Usage

###How to use script
python check.py "filepathtobblearnroster" "filepathtoturingscraftdata" "filepathtoproblemslist" "filepathtoresults" "roster_studentid" "turingscraft_studentid" "problems_id" [-s "sectionid" sectionnumber]

=>

python.exe .\check.py .\sample_roster.csv ..\sample_turingscraft.csv ..\sample_problems.csv ..\sample_result_3.csv Username Email Problems -s Section 3

###How to get BBLearn roster
1. Go to the class page
2. Go to the Grade Center
3. Hover over the "Work Offline" menu and click "Download"
4. Make sure the delimiter type is "Comma"
5. Fill out other options as desired
6. Click "Submit"
7. Click "Download"
8. Save the file where you want it

###How to get Turingscraft roster
1. Go to the course page
2. Click on "Status"
3. Hover over the menu button in the new window that appears and click "Mail Roster"
4. Fill out the form as desired
5. Click submit
6. Acquire file however you desired it and save it where you want

###How to create problems list (Excel)
1. Fill the first row of the first column with a name or column header
2. Fill in the rows of that column with Turingscraft problem ids - short form (12345) not long form (00000-12345)
3. Save as CSV file