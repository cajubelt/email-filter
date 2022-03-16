import csv
from typing import Iterable, Dict, List

FIRST_NAME_COL_NAME = 'Firstname'
EMAIL_COL_NAME = 'Email'
DOMAIN_COL_NAME = 'Domain'

OUTPUT_COL_DELIMITER = '|'

def filter_rows(
        rows: Iterable[Dict[str, str]],
        name_keywords: List[str],
        email_keywords: List[str]
) -> List[Dict[str, str]]:
    return [row for row in rows if
            not row[FIRST_NAME_COL_NAME] in name_keywords and not row[EMAIL_COL_NAME] in email_keywords]


def main():
    input_file_name = input("Enter input tsv file: ")
    output_file_name = input("Enter output txt file: ")
    keywords_name = input("Enter keywords to remove from name list csv file: ")
    keywords_email = input("Enter keywords to remove from email list csv file: ")

    with open(keywords_name, newline='') as f:
        reader = csv.reader(f)
        keyword_list = list(reader)

    keyword_list_name = [row[0] for row in keyword_list]

    with open(keywords_email, newline='') as f:
        reader = csv.reader(f)
        keyword_list = list(reader)

    keyword_list_email = [row[0] for row in keyword_list]

    with open(input_file_name, 'rU', encoding="utf8") as input_file:
        dict_reader = csv.DictReader(input_file, delimiter='\t')
        with open(output_file_name, "w+") as output_file:
            if FIRST_NAME_COL_NAME not in dict_reader.fieldnames:
                raise Exception(f'Missing required column: ${FIRST_NAME_COL_NAME}')
            if EMAIL_COL_NAME not in dict_reader.fieldnames:
                raise Exception(f'Missing required column: ${EMAIL_COL_NAME}')
            include_rows = filter_rows(dict_reader, name_keywords=keyword_list_name, email_keywords=keyword_list_email)
            col_names_ordered = sorted(include_rows[0].keys())
            for row in include_rows:
                f.write(OUTPUT_COL_DELIMITER.join([
                    row[col] for col in col_names_ordered
                ]) + "\n")

    print(f'Wrote ${len(include_rows)} rows to ${output_file_name}')


if __name__=='__main__':
    main()
