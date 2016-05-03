#I plan to get the comments competency checked off on this assignment 
# A sequence of assignments to generate a random problem :
import random
a = random.randint(5,9)
e = random.randint(1,3) #range is kept between 1 and 3 to ensure b remains a single digit integer
c = random.randint(1,3)
d = random.randint(5,9)
b = c * e #b must be calculated this way to counter c * e, leaving only a coefficient for x in the calculation for u
u = (a + (c * d) + (-b + (c * e)))
print('Problem: ({a}x - {b}) + {c}({d}x + {e}) = ?' .format (a = a,
b = b, c = c, d = d, e = e))
print('Answer : {u}x'. format (u = u))

#This is a comment about editing for the staging and committing competency 

#This comment is an edit being made through the GitHub website to demonstrate the pulling competency
