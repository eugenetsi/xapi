#!/usr/bin/python3
# -*- coding: utf-8 -*-

from psycopg2 import connect, Error
import json
from psycopg2.extras import Json
from psycopg2.extras import json as psycop_json
import sys

if len(sys.argv) > 1:
    table_name = '_'.join(sys.argv[1:])
else:
    table_name = "json_data"

print ("\ntable name for JSON data:", table_name)

with open('test_data.json') as json_data:
    record_list = json.load(json_data)

print ("\nrecords:", record_list)
print ("\nJSON records object type:", type(record_list))

sql_string = 'INSERT INTO {} '.format( table_name )

if type(record_list) == list:
    first_record = record_list[0]
    columns = list(first_record.keys())
    print ("\ncolumn names:", columns)
else:
    print ("Needs to be an array of JSON objects")
    sys.exit()

sql_string += "(" + ', '.join(columns) + ")\nVALUES "

for i, record_dict in enumerate(record_list):
    values = []
    for col_names, val in record_dict.items():
        if type(val) == str:
            val = val.replace("'", "''")
            val = "'" + val + "'"
        values += [ str(val) ]
    sql_string += "(" + ', '.join(values) + "),\n"

sql_string = sql_string[:-2] + ";"

print ("\nSQL string:")
print (sql_string)
