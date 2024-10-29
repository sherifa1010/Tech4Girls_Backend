#!/bin/python

#Animals = ['dog','cat','elephant','ant','bird']
#Animals.append()
#print(Animals)

#Animals.remove('elephant')
#print(Animals)

#Animals.reverse()
#print(Animals)

#Animals.sort()
#print(Animals)
#more_Animals = ['sheep','goat']
#Animals.extend(more_Animals)
#print(Animals)


tools = {'pencils','eraser','pen','sharpener','book'}

tools.add('knife')
print(tools)

tools.remove('eraser')
print(tools)

more_tools = {'bag','board'}
tools.union(more_tools)
print(tools)

tools.intersection({'eraser','book'})
print(tools)

tools.difference({'pencils','book'})
print(tools)