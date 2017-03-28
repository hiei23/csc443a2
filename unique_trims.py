import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line
unique_trims = {}
def mapper(record):
    # key: document identifier
    # value: document contents
    value = record[0]
    key = record[1]
    key = key[:-10]
    if key not in unique_trims:
        unique_trims[key] =[value]

    if key in unique_trims:
        if value not in unique_trims[key]:
            unique_trims[key].append(value)
        if value in unique_trims[key]:
            mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts

    nucleotides = list_of_values[0]

    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
