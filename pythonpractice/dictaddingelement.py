thisdict={"brand":"Ford","model":"Mustang","years":1964}
print(thisdict)
del thisdict["model"]
print(thisdict)
#traversal
for x in thisdict :
    print(x,thisdict[x])