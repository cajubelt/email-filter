import argparse
import csv
from typing import Iterable, Dict, List

OUTPUT_COL_DELIMITER = '|'


def filter_rows(
        rows: Iterable[Dict[str, str]],
        name_keywords: List[str],
        email_keywords: List[str],
        name_col_name: str,
        email_col_name: str
) -> List[Dict[str, str]]:
    return [row for row in rows if
            not any(name_keyword.lower() in row[name_col_name].lower() for name_keyword in name_keywords) and
            not any(email_keyword.lower() in row[email_col_name].lower() for email_keyword in email_keywords)]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, help='input TSV file path', required=True)
    parser.add_argument('--output', type=str, help='output file path', default='./data/output.txt')
    parser.add_argument('--name_keywords', type=str, help='File with name keywords to remove',
                        default='./data/KeywordName.csv')
    parser.add_argument('--email_keywords', type=str, help='File with email keywords to remove',
                        default='./data/KeywordEmail.csv')
    parser.add_argument('--name_col_name', type=str, help='Name of the "first name" column', default='Firstname')
    parser.add_argument('--email_col_name', type=str, help='Name of the "email" column', default='Email')
    args = parser.parse_args()

    with open(args.name_keywords, newline='') as f:
        reader = csv.reader(f)
        keyword_list_name = [row[0].lower() for row in list(reader)]

    with open(args.email_keywords, newline='') as f:
        reader = csv.reader(f)
        keyword_list_email = [row[0].lower() for row in list(reader)]

    with open(args.input, 'rU', encoding="utf8") as input_file:
        dict_reader = csv.DictReader(input_file, delimiter='\t')
        with open(args.output, "w+") as output_file:
            if args.name_col_name not in dict_reader.fieldnames:
                raise Exception(f'Missing required column: {args.name_col_name}')
            if args.email_col_name not in dict_reader.fieldnames:
                raise Exception(f'Missing required column: {args.email_col_name}')
            include_rows = filter_rows(dict_reader,
                                       name_keywords=keyword_list_name,
                                       email_keywords=keyword_list_email,
                                       name_col_name=args.name_col_name,
                                       email_col_name=args.email_col_name)
            for row in include_rows:
                output_file.write(OUTPUT_COL_DELIMITER.join([
                    row[col] or '' for col in dict_reader.fieldnames
                ]) + "\n")

    print(f'Wrote {len(include_rows)} rows to {args.output}')


if __name__ == '__main__':
    main()
