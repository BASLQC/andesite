import json
import xmltodict
#!/usr/bin/env python

import sys

# https://pythonadventures.wordpress.com/2014/12/29/xml-to-dict-xml-to-json/
def convert(xml_file, xml_attribs=True):
    with open(xml_file, "rb") as f:    # notice the "rb" mode
        d = xmltodict.parse(f, xml_attribs=xml_attribs)
        return json.dumps(d, indent=2, ensure_ascii=False)
        
print(convert(sys.argv[1]))