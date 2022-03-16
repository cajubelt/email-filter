# email-filter

## Running the script

Run the script by copying this into the command line (PowerShell on Windows, or Terminal on Mac):
```bash
python3 /path/to/project/email_filter.py
```
(Replace `/path/to/project` with the filepath. You can also get this by dragging the file over to PowerShell.)

It will ask for a input file, output file, a csv file containing keywords to elimnate in the name field, and a csv file containing keywords to eliminate in the email field

The input file you can make in google sheets by going to File -> Downlaod -> Tab-separated Values (I had to use this because of all the commas in the data.)

The output file should be a txt file. It will be delimited with a | again due to the commas in the data. You can import this into Excel or Google sheets, just set your delimiter to |.