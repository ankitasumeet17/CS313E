#  File: OfficeSpace.py

#  Description: A company is moving to a larger building. The new office is rectangular and will be subdivided into cubicles.

#  Student Name: Ankita Sumeet 

#  Student UT EID: as96977

#  Course Name: CS 313E

#  Unique Number: A6

#  Date Created: 9/21

#  Date Last Modified: 9/25

import sys

# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle
def area (rect):
    return abs(rect[2]- rect[0]) * abs(rect[3]- rect[1])

# Input: two rectangles in the form of tuples of 4 integers
# Output: a tuple of 4 integers denoting the little rectangle or False
def is_inside(rect1, rect2):
    Big = ()
    Little = ()
    if area(rect1) > area(rect2):
        Big = rect1
        Little = rect2
    else:
        Big = rect2
        Little = rect1

    if (Big[0] < Little[0]) and (Big[1] < Little[1]) and (Big[2] > Little[2]) and (Big[3] > Little[3]):
        return Little
    else:
        return False

# Input: two rectangles in the form of tuples of 4 integers
# Output: a tuple of 4 integers denoting the overlapping rectangle.
#         return (0, 0, 0, 0) if there is no overlap
def overlap (rect1, rect2):
    # if inside 
    if is_inside(rect1, rect2) != False:
        print(is_inside(rect1, rect2))

    if rect1[0] < rect2[0] < rect1[2] and rect1[1] < rect2[1] < rect1[3]: 
        return (rect2[0], max(rect1[1],rect2[1]), min(rect1[2],rect2[2]),min(rect2[3],rect1[3]))
    if rect2[0] < rect1[0] < rect2[2] and rect2[1] < rect1[3] < rect2[3]: 
        return (rect2[0], max(rect1[1],rect2[1]), min(rect1[2],rect2[2]),min(rect2[3],rect1[3]))
    else:
        return (0, 0, 0, 0)


# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the unallocated 
#         space in the office
def unallocated_space (bldg):
    un = 0
    for i in range(len(bldg)):
        for j in range(len(bldg[i])):
            if bldg[i][j] == 0:
                un += 1
    return un

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the contested 
#         space in the office
def contested_space (bldg):
    cont = 0
    for i in range(len(bldg)):
        for j in range(len(bldg[i])):
            if bldg[i][j] >= 2:
                cont += 1
    return cont  

# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
# Output: a single integer denoting the area of the uncontested 
#         space in the office that the employee gets
def uncontested_space (bldg, rect):
    un = 0
    for i in range(rect[0], rect[2]):
        for j in range(rect[1], rect[3]):
            if bldg[j][i] == 1:
                un += 1
    return un

# Input: office is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing all
#        the requested cubicles
# Output: a 2-D list of integers representing the office building and
#         showing how many employees want each cell in the 2-D list
def request_space (office, cubicles):
    ws = [[0 for x in range(office[2])]
                   for y in range(office[3])] 
    for i in range(len(cubicles)):
        for x in range(int(cubicles[i][0]), int(cubicles[i][2])):
            for y in range(int(cubicles[i][1]), int(cubicles[i][3])):
                ws[y][x] += 1

    return ws

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
  ''' assert area ((0, 0, 1, 1)) == 1
  # write your own test cases

  return "all test cases passed" '''

def main():
  # read the data
    line = sys.stdin.readline().strip()
    line = line.split()
    w = line[0]
    h = line[1] 

    #number of employees 
    n = sys.stdin.readline().strip()
    office = (0, 0, int(w), int(h))
    cubicles = []
    employes = []

    for t in range(int(n)):
        employee = sys.stdin.readline().strip().split()
        emp = int(employee[1]), int(employee[2]), int(employee[3]), int(employee[4])
        cubicles.append(emp)
        employes.append(employee[0])
    
    req = request_space(office,cubicles)

  # run your test cases
    ''' print (test_cases()) '''

  # compute the total office space
    print('Total' , area(line))

  # compute the total unallocated space
    print('Unallocated' , unallocated_space (req))

  # compute the total contested space
    print('Contested' , contested_space (req))

  # compute the uncontested space that each employee gets
    for i in range(len(cubicles)):
        uncontest = uncontested_space(req,cubicles[i])
        print(employes[i],uncontest)

if __name__ == "__main__":
  main()            

