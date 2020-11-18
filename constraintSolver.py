# Joe Malone
# Dominic DuRant
from z3 import *
import itertools

class constraintSolver:
    # Return array of people and number of conflicting
    # pairs
    def createDep():
        i = 0
        store = []
        hasInput = True
        while (hasInput == True):
            # Split each department input
            people, pairs =  input().split()
            i = int(pairs)

            # Stop condition
            if (int(people) == 0 and int(pairs)== 0):
                break

            conflictsList = []

            # Append conflicts
            conflictsList.append(int(people))
            while(int(i) > 0):    
                person1, person2 = input().split()
                conflictsList.append((int(person1),int(person2)))
               
                i = i - 1
            
            store.append(conflictsList)
       
        return store

    def constraint():
        # returns a list of departments. The first number
        # is the number of people in the department. The following
        # touples are the pairs that don't get along.
        # Example ((7, (1,2), (3, 4)), (5, (1,2), (2, 4)))
        dep = constraintSolver.createDep()

        for department in dep:
            size = department[0]
            
            n = 1          
            while n <= size:
                s = z3.Solver()
                f = Function('f', IntSort(), IntSort())

                # Constrain the number of committees to be between 1 and n
                for i in range(1, size+1):
                    s.add(f(i) >= 1, f(i) <= n)

                # Add the conflict constraints
                for i in range(1,len(department)):
                    s.add(f(department[i][0]) != f(department[i][1]))
    

                if s.check() == z3.sat:
                    print (n)
                    break                  
                
                n = n + 1
                
constraintSolver.constraint()