import csv

FIRST_NAME_COL_NAME = 'Firstname'
EMAIL_COL_NAME = 'Email'
DOMAIN_COL_NAME = 'Domain'

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

    dict_reader = csv.DictReader(tsv_file, delimiter='\t')

    if FIRST_NAME_COL_NAME not in dict_reader.fieldnames:
        raise Exception(f'Missing required column: ${FIRST_NAME_COL_NAME}')
    if EMAIL_COL_NAME not in dict_reader.fieldnames:
        raise Exception(f'Missing required column: ${EMAIL_COL_NAME}')

    for row in dict_reader:

        remove = False

        name = row[FIRST_NAME_COL_NAME]
        email = row[EMAIL_COL_NAME]
        domain = row[DOMAIN_COL_NAME]

        for word in keyword_list_name:
            if word[0] in name:
                remove = True

        for word in keyword_list_email:
            if word[0] in email:
                remove = True

        if not remove:
            f.write(name + "|" + email + "|" + domain + "\n")
f.close()
