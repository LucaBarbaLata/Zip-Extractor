from zipfile import ZipFile

choice = input('Whats the name of the archive?\n')
with ZipFile(choice + ".zip", 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall("Extracted files!")