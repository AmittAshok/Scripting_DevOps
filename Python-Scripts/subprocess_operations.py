# subprocess module is use for running shell commamds in system

import subprocess
import sys

result = subprocess.run( ['ls', '-l'], capture_output=True, text=True)
result1 = subprocess.run( ['free', '-h' ] , capture_output=True, text=True)

print("output: \n ", result.stdout)
print("memoy: /n ", result1.stdout)

if result.stderr:
    print("Error", result.stderr)
else:
        print("completed list")
        