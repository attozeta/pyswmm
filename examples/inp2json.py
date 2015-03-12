#!/usr/bin/python
import sys
import swmm
import json

r, data = swmm.parse(sys.stdin)
if not r:
    print('fatal: ' + data)
    sys.exit(1)

inp = json.dumps(data)
print(inp)

