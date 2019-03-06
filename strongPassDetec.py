import re

def passTest(string):
    char8 = re.compile(r"[A-Z0-9]\w{8,}")
    mo = char8.search(string)
    if mo != None:
        print("Good pass")
    else:
        print("Fail")


pwd = "Patorras6"
pwd01 = "patorras5"
pwd02 = "Patorras"
pwd03 = "zemane"

passTest(pwd01)
passTest(pwd)
