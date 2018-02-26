# Count-Log
A simple script to parse ocurrences in a given log file, using regex patterns and printing it;

## Usage
The script depends on search.ini file, the ini file will contain the structure of regex and some output patterns

Example:
```
$ ./count_log.py -t HTTP -r CODE
200 845
304 58
302 26
206 11
401 3
499 1
```

Basically, the script parses the following lines to get the number of occurrences of the status code on teste.log file

```
[LOG]
FILE = ./teste.log

[METRIC]
TYPE = raw

[HTTP]
CODE = HTTP\S+\s+(\d{3})
```

## To Do
-Create and organize functions
-Better code commentary
-Create more output patterns
