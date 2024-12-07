import subprocess
import sys

result = subprocess.run( ['ls', '-l'], capture_output=True, text=True)

print("output: \n ", result.stdout)

if result.stderr:
    print("Error", result.stderr)