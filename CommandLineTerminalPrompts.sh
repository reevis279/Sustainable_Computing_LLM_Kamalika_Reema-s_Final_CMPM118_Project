Command Line Terminal Prompts to remember

--To turn on virtual environment--
Be in correct directory and run this:
source [name]/bin/activate

--GLANCES--
To open:
glances 
To open glances csv file:
cat [name of file].csv 

---To make glances give less information and run quietly in background--
glances --export csv --export-csv-file /tmp/glances.csv --disable-plugin all --enable-plugin cpu,mem,load --quiet

---To make glances give less information and run quietly and stop after 5 seconds--
glances --export csv --export-csv-file ./glances_output.csv --disable-plugin all --enable-plugin cpu,mem,load --quiet --stop-after 5

--To look at the first few columns in the .csv file--
head -n 5 glances_output.csv | cut -d, -f1-10

--To check the data of the last few rows in the .csv file--
tail -n 5 glances_output.csv | cut -d, -f1-10


