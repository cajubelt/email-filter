import csv

input_file = input("Enter input tsv file: ")
output_file = input("Enter output txt file: ")
keywords_name = input("Enter keywords to remove from name list csv file: ")
keywords_email = input("Enter keywords to remove from email list csv file: ")

with open(keywords_name, newline='') as f:
    reader = csv.reader(f)
    keyword_list = list(reader)

keyword_list_name = keyword_list

with open(keywords_email, newline='') as f:
    reader = csv.reader(f)
    keyword_list = list(reader)

keyword_list_email = keyword_list

with open(input_file, 'rU', encoding="utf8") as tsv_file:
    f = open(output_file, "w+")

    read_csv = csv.reader(tsv_file, delimiter='\t')
    row_count = sum(1 for row in read_csv)

    tsv_file.seek(0)
    next(read_csv)

    for ct, row in enumerate(read_csv):

        remove = False

        name = row[7]
        email = row[5]
        domain = row[0]

        for word in keyword_list_name:

            if word[0] in name:
                remove = True

        for word in keyword_list_email:

            if word[0] in email:
                remove = True

        if not remove:
            f.write(name + "|" + email + "|" + domain + "\n")
        print(remove)
f.close()
