import argparse
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
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, help='input TSV file path', required=True)
    parser.add_argument('--output', type=str, help='output file path', default='./data/output.txt')
    parser.add_argument('--name_keywords', type=str, help='File with name keywords to remove',
                        default='./data/KeywordName.csv')
    parser.add_argument('--email_keywords', type=str, help='File with email keywords to remove',
                        default='./data/KeywordEmail.csv')
    args = parser.parse_args()

    with open(args.name_keywords, newline='') as f:
        reader = csv.reader(f)
        keyword_list_name = [row[0] for row in list(reader)]

    with open(args.email_keywords, newline='') as f:
        reader = csv.reader(f)
        keyword_list_email = [row[0] for row in list(reader)]

    with open(args.input, 'rU', encoding="utf8") as input_file:
        dict_reader = csv.DictReader(input_file, delimiter='\t')
        with open(args.output, "w+") as output_file:
            if FIRST_NAME_COL_NAME not in dict_reader.fieldnames:
                raise Exception(f'Missing required column: {FIRST_NAME_COL_NAME}')
            if EMAIL_COL_NAME not in dict_reader.fieldnames:
                raise Exception(f'Missing required column: {EMAIL_COL_NAME}')
            include_rows = filter_rows(dict_reader, name_keywords=keyword_list_name, email_keywords=keyword_list_email)
            for row in include_rows:
                output_file.write(OUTPUT_COL_DELIMITER.join([
                    row[col] or '' for col in dict_reader.fieldnames
                ]) + "\n")

    print(f'Wrote {len(include_rows)} rows to {args.output}')


if __name__ == '__main__':
    main()
