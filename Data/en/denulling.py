#!/usr/bin/python3
# Reprocess the JSON to use value 0 rather than just nonexistence
import json
import sys

# open the filename specified as first argument
fname = sys.argv[1]
with open(fname, "r") as f:
	json_data = json.load(f)

# get all known possible keys
all_keys = set().union(*(d.keys() for d in json_data))

# set null keys to value 0 rather than just nonexistence
for item in json_data:
	for key in all_keys:
		if key not in item:
			item[key] = 0

# write fixed version to the original file
with open(fname, "w") as f:
	f.write(json.dumps(json_data, indent=2, ensure_ascii=False))
