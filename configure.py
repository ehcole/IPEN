import os
import fileinput
pwd = os.getcwd()
path = str()
for char in pwd:
  if char != '\\':
    path += char
  else: 
    path += '/'
# Does a list of files, and
# redirects STDOUT to the file in question
for line in fileinput.input(os.listdir(path + "/post-processing"), inplace = 1): 
      print line.replace('.', path),
  
