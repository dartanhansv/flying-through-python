# Working with files


# Writing
"""
myVar = open('file_name', 'w')     # open the file
print(myVar.write())               # write
myVar.close()                      # close
"""

# Reading
"""
myVar = open('file_name', 'r')     # open the file
print(myVar.read())                # read
myVar.close()                      # close
"""


# mode wra
"""
'w' = write
'r' = read
'a' = append
"""


performances = {
    "Ventriloquism": "9:00am",
    "Snake Charmer": "12:00pm",
    "Amazing Acrobatics": "2:00pm",
    "Enchanted Elephants": "5:00pm",
}

try:
    schedule_file = open("schedule.txt", "w")
except (
    FileNotFoundError
) as err:  # Create a val called 'err' and store the error message
    print(err)
for key, val in performances.items():
    schedule_file.write(key + " - " + val + "\n")

schedule_file.close()
"""

file1 = open("schedule_file.txt")
print(file1.read())

file1.close()
"""
