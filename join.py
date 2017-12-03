import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[1]
    value = record

    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts

    line_item_tuples = []
    order_tuples = []
    
    for v in list_of_values:

        if (v[0] == "line_item"):
            line_item_tuples += [v]
        else:
            order_tuples +=[v]
        
    for o in order_tuples:
        for l in line_item_tuples: 
            joined_row = o+l
            mr.emit(joined_row)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
