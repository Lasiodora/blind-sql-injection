# blind-sql-injection

options:
  -h, --help    show this help message and exit
  -u U          Enter URL
  -param PARAM  Data string to be sent through POST (e.g. "id","name", etc...)

To change the output of the columns, you need to edit the first digit in the
string "limit 0,1" (0 for the first column). If you set "limit 1,1", u see
second column. Similarly for tables and values in the database. To ennumerate,
unlock the corresponding row with # in code.
