import os







import fileinput







pwd = os.getcwd()







path = str()







for char in pwd:







  if char != '\\':







    path += char







  else: 







    path += '/'







os.system("mv " + path + "/experimental_data " + path[:-16])







# Does a list of files, and







# redirects STDOUT to the file in question







for line in fileinput.input(os.listdir(path), inplace = 1):



#  print(line.replace("\'.\'", "'" + path[:-16] + "'"))



  if "pathToTopLevel =" in line and not ":" in line:



    print(line.split("=")[0] + "= '" + path[:-16] + "'")



  else:



    print(line)











os.system("mv " + path[:-16] + "/experimental_data " + path) 







