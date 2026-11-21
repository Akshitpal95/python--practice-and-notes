# List, Tuple, Set, Dictionary

#previous primitive: int, bool, float, str
#Right now Complex: List, Tuple, Set, Dictionary


#                           LIST                             

#list : print(marks, type(marks))

#length : print(len(marks))

#index print(marks[2]), print(marks[-1]): means value of last / previous index

#Slicing a list - list[st:end] :: print(marks[0:3]) , print(makrs[-3:]): means from -3 to till the index ends

#marks.append : add a value to the end of the list present ,marks.insert (1,50) : 1 means adding value in front of index 1 ,50: is the value added , we also have marks.clear to delete whole list


#                          TUPLE

#tuple is immutable cant be modified ex: marks: (98, 99, 97, 95, 93) print(marks, type(marks))


# operation : print(marks.count(95)) , print(marks.index(93)) , marks 



#                           SET

# collection of unique items

# marks = {98, 97, 96, 95 ,94}

# print(len(marks, marks)) 

# for score in marks:
#   print(score)


#                           DICTIONARY

# {key => val}

# marks = {"Maths": 99, "physics": 97}
# print(marks, type(marks)) 

# print(marks["Physics"])

# marks["English"] = 95

# print( marks["English"])

# # loops in dictionary

# for key in marks:
#   print(key, marks[key])

# temp data : stored inlist , permanent data stored in tuple