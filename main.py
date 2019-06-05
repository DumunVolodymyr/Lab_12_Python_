import re

def read_file():
    with open("file.txt") as file:
        results = re.findall("23/Mar/2009"
                       #"([0-0][2-5]:[0-5][0-5]:[0-0][2-3])"
                       ".*.php"
                       ".* 3[0-9][0-9] "
                             ,
                             file.read())

    for i in results:
        print(results, "\n")
    for isd in range(20):
        print(isd)

read_file()