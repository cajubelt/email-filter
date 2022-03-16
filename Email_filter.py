import csv
import os

inputfile = input("Enter input tsv file: ")
outputfile = input("Enter output txt file: ")
keywordsname = input("Enter keywords to remove from name list csv file: ")
keywordsemail = input("Enter keywords to remove from email list csv file: ")


with open(keywordsname, newline='') as f:
    reader = csv.reader(f)
    keywordlist = list(reader)

keywordlistname = keywordlist

with open(keywordsemail, newline='') as f:
    reader = csv.reader(f)
    keywordlist = list(reader)

keywordlistemail = keywordlist

with open(inputfile, 'rU', encoding="utf8") as csvfile:
    
    f= open(outputfile,"w+")
    
    readCSV = csv.reader(csvfile, delimiter='\t')
    row_count = sum(1 for row in readCSV)

    csvfile.seek(0)
    next(readCSV)

    for ct, row in enumerate(readCSV):

        remove = False

        name = row[7]
        email = row[5]
        domain = row[0]

        for word in keywordlistname:

            if word[0] in name:
                remove = True

        for word in keywordlistemail:

            if word[0] in email:
                remove = True

        if not remove:
            f.write(name+"|"+email+"|"+domain+"\n")
        print(remove)
f.close()
