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

--To display stats in CSV formate cleanly--
glances --stdout-csv now,cpu.user,mem.used,load

--To display stats in CSV formate cleanly for ____ seconds--
glances --stdout-csv now,cpu.user,mem.used,load --stop-after _____

--To display stats for a specific process in graph format:--
1. Create Glances config file: mkdir -p ~/.config/glances inside your virtual environment
2. cd ~/.config/glances
3.ls  
4. nano glances.conf OR vim glances.conf
5. glances --export graph --export-graph-path /tmp
6. While glances is running press g and then enter to open the process path prompt
7. Type in the name of the process you want to monitor (for example *.ollama.*)
6. if it gives you an error do pip install pygal or whatever you use to install python packages (pygal)
7. open the file using xdg-open /tmp/cpu.svg or if that doesn't work try finding it in your file explorer (it will be in your linux folder)


