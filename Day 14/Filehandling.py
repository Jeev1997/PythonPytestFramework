
# with open("C:\\Filehandling\\myfile.txt", 'w') as file:
#  file.write("this is a test \n this is first file")
#  file.close()

# Append
# with open("C:\\Filehandling\\myfile.txt", 'a') as file:
#  file.write("\n this is a testing")
#  file.close()

# Read
#read( )--- read all the lines
#readline()-- single line
#readlines() -- read and return in list format

# with open("C:\\Filehandling\\myfile.txt", 'r') as file:
#  # content = file.read()
#  # content = file.readline()
#  content = file.readlines()
#  print(content)
#  file.close()


#Rename file

import os
os.rename("C:\\Filehandling\\myfile.txt", "C:\\Filehandling\\myfile123.txt")
print("success")




