# email-filter

## Running the script

Run the script by copying this into the command line (PowerShell on Windows, or Terminal on Mac):
```bash
cd /path/to/project
python3 email_filter.py --input=./input-file-name.tsv --output=./output-file-name.tsv --name_keywords=./name-keywords-file-name.csv --email_keywords=./email-keywords-file-name.csv
```
For the above^, replace `/path/to/project` with the filepath and the file names with the relevant file names. You can also get the filepath by dragging the folder where the script lives over to PowerShell.

The input file you can make in google sheets by going to File -> Downlaod -> Tab-separated Values (I had to use this because of all the commas in the data.)

The output file should be a txt file. It will be delimited with a | again due to the commas in the data. You can import this into Excel or Google sheets, just set your delimiter to |.