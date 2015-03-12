#!/usr/bin/python
import sys
import swmm

r, data = swmm.parse(sys.stdin)
if not r:
    print('fatal: ' + data)
    sys.exit(1)

swmm.prettyprint(sys.stdout, data)

