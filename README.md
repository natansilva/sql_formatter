# SQL Formatter

[![Build Status](https://travis-ci.com/natansilva/sql_formatter.svg?branch=master)](https://travis-ci.com/natansilva/sql_formatter) [![Codecov Status](https://codecov.io/gh/natansilva/sql_formatter/branch/master/graphs/badge.svg)](https://codecov.io/gh/natansilva/sql_formatter/)

A Simple SQL Formatter. Builded to to a better read.

## USAGE
Install this with pip using this command: `pip install simple-sql-formatter`
In a python file import the module like this: `import formatter.formatter as fm`
Use `format_string()` function from this module to format queries and be happy.

## EXAMPLE
```python
import formatter.formatter as fm

print(fm.format_string('select campo1, campo2, campo3 from tabela'))
```

The output like this:
```sql
SELECT
    campo1
  , campo2
  , campo3
FROM tabela
```


## TODO
Create a configuration for choose the layout of queries.
