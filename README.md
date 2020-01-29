# passwrd_cracker
#####Simple Password Cracker made with Python by Josh Gilley and Chris Taylor

###There are two ways to run the program.
1. You may use our testing and you will not have to provide your own files
2. You may provide your own files with your passwords in a specific format
follow instructions below for either way

##Run using our testing
1. Start up the program in your ide of choice
2. Make sure there are 2 files called "test_in.txt" and "test_out.txt"
3. These are used for the tests we have made.
4. Run the tests.py program
5. You should see output through the IDE terminal showing what passwords it was able to crack.
6. You can look at the "test_out.txt" to see a list of the passwords it tried to/succesfully cracked.

## Run using your own input and output file
1. The first step is to make sure that your file storing your hashes is in the correct format. 
(If it is not, the program will run not run correctly)
The correct format for the file is for each line to have its own password stored in user:
hashcode:other information

2. Run Gilley_Taylor_HW1_passwd_cracking.py

3. A command prompt will pop up in the IDE. Type in your in file and hit enter. Then type your
out file and hit enter.

4. The program will begin to try and crack the passwords in your in file. 

5. When it is finished it will output a total time it took to crack all the passwords
as well as a message saying that the passwords were written to your specified text file.
