# Change-File-Name-by-Date
This code takes a folder with files of any naming scheme, uses datefinder (@akoumjian) to extract dates, deduces whether or not that date # is viable, and renames the file with the correct date. It also allows you to put files that were not changed into a different folder so you can manually change them.

This would not be good for a file that has a ton of numbers, as datefinder can't extract dates from a file name like:
     LN_174365_CB_A4248_OE_11xx_15xx_HLKn_wsw001_06032019_v2
I've limited it to a file that, if you combine all the digits, has less than 9 digits total, the max being the longest numbered date:
     mm-dd-yyyy
  
so far the cases I've excluded from changing are:

- when the year datefinder finds is past the current year
- when the file name only has month and date (anything less than 1231) or has no numbers or too many (9 or more, see example above)
- when the file has 2 or more spaces in the string that datefinder is using to extract and it doesn't contain letters (2018 dec 6 would be okay)
- when the date found for the current file is the exact same date found for the last file
- when datefinder cannot find a date
