import os
import re
import datefinder # using akoumjian's datefinder library on github
                  # https://datefinder.readthedocs.io/en/latest/
import datetime as d

print "Enter the complete folder path for your files, ex: /User/folder/"
myFolder = raw_input('')
print "Enter the complete folder path for the files that will need to be done manually"
print "If you don't want to move your files, put the same folder"
manualFolder = raw_input('')

os.chdir(myFolder)
files = os.listdir(myFolder)
total_renamed = 0  # type: int
sameDateCheck = datefinder.find_dates("", index=True)

for i in range(len(files)):
    filename, file_extension = os.path.splitext(files[i])
    haveNumbers = ''.join(y for y in filename if y.isdigit())

    # if date is only month and day or has too many numbers to be a date or if file has no numbers
    if len(haveNumbers) <= 0 or int(haveNumbers) <= 1231 or len(haveNumbers) > 9:
        os.rename(myFolder + "/" + filename + file_extension, manualFolder + "/" + filename + file_extension)
        continue

    matches = datefinder.find_dates(filename, index=True)
    for match in matches:
        x = match
        print x
    try:
      # check if x is defined
      x
    except NameError:
      print "datefinder could not find a date"
      # put it in the folder for manual renaming if not
      os.rename(myFolder + "/" + filename + file_extension, manualFolder + "/" + filename + file_extension)
      continue

    if x == sameDateCheck:
        os.rename(myFolder + "/" + filename + file_extension, manualFolder + "/" + filename + file_extension)
        continue
    sameDateCheck = x
    # get date from datetime object without timestamp
    dateTooLong = str(x[0])
    newDate = dateTooLong.strip(" 00:00:00")
    yearFound = dateTooLong[0:4]  # type: str

    # get string from filename that the datetime object used and delete leading/trailing spaces
    # if string has more than 2 spaces and no letters, or date is exactly the same as previous entry
    # put it in the folder for manual renaming
    firstIndex = int(x[1][0])  # type: int
    secondIndex = int(x[1][1])  # type: int
    dateFound = filename[firstIndex:secondIndex]  # type: str
    dateFound = dateFound.strip()
    hasSpaces = ''.join(y for y in dateFound if y.isspace())
    if int(len(hasSpaces)) >= 2 and re.search('[a-zA-Z]+', dateFound) == None:
        os.rename(myFolder + "/" + filename + file_extension, manualFolder + "/" + filename + file_extension)
        continue

    # replace filename if it's not past current year or before the 15th century
    c_year = str(d.datetime.now().year)
    if int(yearFound) <= int(c_year) and int(yearFound) >= 1400:
        dateString = filename[firstIndex:secondIndex]
        updatedName = filename.strip(dateString)
        finalString = newDate + " " + updatedName
        print finalString
        total_renamed += 1
        os.rename(files[i], finalString + file_extension)
    else:
        # otherwise, put it in the folder for manual renaming
        os.rename(myFolder + "/" + filename + file_extension, manualFolder + "/" + filename + file_extension)
print total_renamed
