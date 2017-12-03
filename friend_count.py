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
    mr.emit_intermediate(1, record)


def reducer(key, list_of_values):
    friend_list = {}
    true_friends = {}

    for friend in list_of_values:
        friendA = friend[0]
        friendB = friend[1]

        if friendA in friend_list:
            friend_list[friendA] += [friendB]

        if friendA not in friend_list:
            friend_list[friendA] = [friendB]
            true_friends[friendA] = 0

        if friendB not in friend_list:
            friend_list[friendB] = []
            true_friends[friendB] = 0

        # check if they are true friends
        if friendA in friend_list[friendB] and friendB in friend_list[friendA]:
        	true_friends[friendA] += 1
        	true_friends[friendB] += 1

    for name, count in true_friends.items():
    	mr.emit((name, count))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
