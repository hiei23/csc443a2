import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

#global variable to keep track of friends locally
friend_list = {}
def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]

    if key not in friend_list:
        friend_list[key] =[value]

    if key in friend_list:
        if value not in friend_list[key]:
            friend_list[key].append(value)
        if value in friend_list[key] and value in friend_list:
            if key in friend_list[value]:
                mr.emit_intermediate(key, value)
                mr.emit_intermediate(value, key)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    mr.emit((key, list_of_values))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
