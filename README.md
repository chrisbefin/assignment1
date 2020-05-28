<b>This is the first assignment for LASP summer training 2020. <br>
<b>assignment description:<br>
The assignment consists of two seperate tasks. First, you must write a python script which parses an excerpt of a Shakespeare play in 
plain text format. The play script must be reformatted such that all of a character's lines appear together and all characters are listed
in alphabetic order. Additionally, for each character, a number of spoken words and a most frequently spoken word must be found. This means
that stage direction and other non spoken words appearing in the input text must be parsed out. The second task consists of writing a
number of python classes. Beginning with a generic 'Planet' class, 9 classes must also be made for each planet in the solar system which
inherit from the 'Planet' class. Finally, a super 'SolarSystem' class must be made, which has all 9 planet objects as data members.<br>
<b>File descriptions:<br>
read_script.py: python file which parses an inputted play script and writes formatted output to a specified output file. <br>
alls_well_that_ends_well.txt: this file contains the play excerpt that is to be parsed by read_script.py<br>
output.txt: this is a text file where output can be written<br>
classes.py: This file contains declarations for all the classes required for part 2 of the assignment described above. This only has class
definitions and no other python, so it must be interpreted from the interactive shell in order for classes to be instantiated.<br>

<b>Execution instructions:<br>
  for read_script.py: python read_script.py \<path to input file\> \<path to output file\><br>
  for classes.py: python -i classes.py<br>
