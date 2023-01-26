#  File: Geometry.py

#  Description: This program develops several classes that are fundamental in Solid Geometry - Point, Sphere, Cube, and Cylinder. In main() we test the various functions that we have written for the classes.

#  Student Name: Ankita Sumeet

#  Student UT EID: as96977

#  Partner Name: Sakshee

#  Partner UT EID: smj2855

#  Course Name: CS 313E

#  Unique Number: A4

#  Date Created: 9/15

#  Date Last Modified: 9/17

import math
import sys

class Point (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0):
      self.x = float(x)
      self.y = float(y)
      self.z = float(z)

  # create a string representation of a Point
  # returns a string of the form (x, y, z)
  def __str__ (self):
      return '(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'

  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
  def distance (self, other):
      return math.hypot (self.x - other.x, self.y - other.y, self.z - other.z)

  # test for equality between two points
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):
      tol = 1.0e-6
      return (abs (self.x - other.x) < tol) and (abs (self.y - other.y) < tol) and (abs (self.z - other.z) < tol)

#---------------------------------------------------------------------------------------

class Sphere (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
    self.x = float(x)
    self.y = float(y)
    self.z = float(z)
    self.radius = float(radius)
    self.center = Point(x,y,z)

  # returns string representation of a Sphere of the form:
  # Center: (x, y, z), Radius: value
  def __str__ (self):
    return "Center: (" + str(self.x) +", " + str(self.y)+", " +str(self.z) + ")," + " Radius: " + str(self.radius)

  # compute surface area of Sphere
  # returns a floating point number
  def area (self):
    # 4 pi r^2
    return (self.radius ** 2) * 4 * math.pi

  # compute volume of a Sphere
  # returns a floating point number
  def volume (self):
    # 4/3 pi r^3
    return (4/3) * math.pi * (self.radius **3)

  def get_maxes(self):
    # A max is = to center x,y, or z + the radius
    x_max = self.center.x + self.radius
    y_max = self.center.y + self.radius
    z_max = self.center.z + self.radius
    return (x_max, y_max, z_max)

  def get_mins(self):
    # A min is = to center x,y, or z - the radius
    x_min = self.center.x - self.radius
    y_min = self.center.y - self.radius
    z_min = self.center.z - self.radius
    return (x_min, y_min, z_min)


  # determines if a Point is strictly inside the Sphere
  # p is Point object
  # returns a Boolean
  def is_inside_point (self, p):
    return self.center.distance(p) < self.radius
    # if min/max of point is within mix/max of sphere

  # determine if another Sphere is strictly inside this Sphere
  # other is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, other):
    #print(other)
    #print(self.center)
    #print(other.center)
    dist_center = self.center.distance(other.center)
    return (dist_center + other.radius) < self.radius
    # if min/max of smol sphere is within mix/max of big sphere
    # bs min (L) < sm min < ss max < bs max [if all true]
    # do we need to compare volume

  # determine if a Cube is strictly inside this Sphere
  # determine if the eight corners of the Cube are strictly
  # inside the Sphere
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
    #dist_center = self.center.distance(a_cube.center)
    #return (dist_center - a_cube.radius) > self.radius
    verticies_list = a_cube.verticies()
    for x in verticies_list:
      if((x.distance(self.center) < self.radius) == False):
        return False
    return True
    # call the point def

  def is_outside_cube(self, a_cube):
    lst = []
    xmin = Point(self.center.x - self.radius,self.y,self.z)
    lst.append(xmin)
    xmax = Point(self.center.x + self.radius,self.y,self.z)
    lst.append(xmax)
    ymin = Point(self.x,self.center.y - self.radius,self.z)
    lst.append(ymin)
    ymax = Point(self.x,self.center.y + self.radius,self.z)
    lst.append(ymax)
    zmin = Point(self.x,self.y,self.center.z - self.radius)
    lst.append(zmin)
    zmax = Point(self.x,self.y,self.center.z + self.radius)
    lst.append(zmax)

    for x in lst:
      if(self.a_cube.is_outside_point(x) == False):
        return False

    allverticies = self.verticies()
    for z in allverticies:
      if(self.center.distance(z) < self.radius):
        return False

    return True


  # determine if a Cylinder is strictly inside this Sphere
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cyl (self, a_cyl):

    other_maxes = a_cyl.get_maxes()
    other_mins = a_cyl.get_mins()

    self_maxes = self.get_maxes()
    self_mins = self.get_mins()

    # checks to see if cyl's maxes and mins are inside the sphere's maxes and mins
    if self_mins[0] < other_mins[0] < other_maxes[0] < self_maxes[0] and \
            self_mins[1] < other_mins[1] < other_maxes[1] < self_maxes[1] and \
            self_mins[2] < other_mins[2] < other_maxes[2] < self_maxes[2]:

        is_inside = True

    else:

        is_inside = False

    return is_inside

  # determine if another Sphere intersects this Sphere
  # other is a Sphere object
  # two spheres intersect if they are not strictly inside
  # or not strictly outside each other
  # returns a Boolean
  def does_intersect_sphere (self, other):

    if self.is_inside_sphere(other) == False and \
        other.is_inside_sphere(self) == False and \
        Cylinder.is_outside(self, other) == False:

        intersect = True

    else:

        intersect = False

    return intersect

  # determine if a Cube intersects this Sphere
  # the Cube and Sphere intersect if they are not
  # strictly inside or not strictly outside the other
  # a_cube is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, a_cube):

    if self.is_inside_cube(a_cube) == False and \
            a_cube.is_inside_sphere(self) == False and \
            Cylinder.is_outside(self, a_cube) == False:

        intersect = True

    else:

        intersect = False

    return intersect

    '''if not is_inside_cube and not outside
    if( self.center.is_outside_cube(a_cube) == "True" and self.center.is_inside_cube(a_cube) == "True"):
      return False

    return self.center.distance(a_cube) < (self.radius + a_cube.radius)'''

  # return the largest Cube object that is circumscribed
  # by this Sphere
  # all eight corners of the Cube are on the Sphere
  # returns a Cube object
  def circumscribe_cube (self):

    diameter = self.radius * 2
    side = (diameter / (math.sqrt(3)))

    cube = Cube(self.center.x, self.center.y, self.center.z, side)

    return cube


#---------------------------------------------------------------------------------------

class Cube (object):
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.

  #function that gives you back the coordinate of all 8 verticies

  def __init__ (self, x = 0, y = 0, z = 0, side = 1):
    self.x = float(x)
    self.y = float(y)
    self.z = float(z)
    self.side = float(side)
    self.center = Point(x,y,z)

  # string representation of a Cube of the form:
  # Center: (x, y, z), Side: value
  def __str__ (self):
    return "Center: (" + str(self.x)+", "+ str(self.y)+", " +str(self.z)+ "), " + "Side: " + str(self.side)

  # compute the total surface area of Cube (all 6 sides)
  # returns a floating point number
  def verticies(self):
    self.lst = []
    half_side = self.side /2
    # add .5 side to x coordinate both front and back
    coor1 = Point(self.x + half_side, self.y + half_side, self.z - half_side )
    self.lst.append(coor1)
    coor2 = Point(self.x + half_side, self.y - half_side, self.z - half_side)
    self.lst.append(coor2)
    coor3 = Point(self.x - half_side, self.y - half_side, self.z - half_side)
    self.lst.append(coor3)
    coor4 = Point(self.x - half_side, self.y  + half_side, self.z - half_side)
    self.lst.append(coor4)
    coor5 = Point(self.x - half_side, self.y - half_side, self.z  + half_side)
    self.lst.append(coor5)
    coor6 = Point(self.x - half_side, self.y + half_side, self.z  + half_side)
    self.lst.append(coor6)
    coor7 = Point(self.x + half_side, self.y - half_side, self.z  - half_side)
    self.lst.append(coor7)
    coor8 = Point(self.x + half_side, self.y + half_side, self.z  - half_side)
    self.lst.append(coor8)
    return self.lst
    # add .5 side to y coordinate front and back
    # add .5 side to z coordinate and front and back

  def area (self):
    # 6 side^2
    return (self.side ** 2) * 6

  # compute volume of a Cube
  # returns a floating point number
  def volume (self):
    # a^3
    return self.side ** 3

  def get_maxes(self):

        maxes = []
        half_side = self.side / 2

        maxes.append(self.center.x + half_side)
        maxes.append(self.center.y + half_side)
        maxes.append(self.center.z + half_side)

        return maxes

  # gets minimum x,y, and z values for the cube
  def get_mins(self):

      mins = []
      half_side = self.side / 2

      mins.append(self.center.x - half_side)
      mins.append(self.center.y - half_side)
      mins.append(self.center.z - half_side)

      return mins


  # determines if a Point is strictly inside this Cube
  # p is a point object
  # returns a Boolean
  def is_inside_point (self, p):
    #return self.center.distance(p) <=
    #point to be inside the cube
    # x max and x min, y and z and you want point to be inside the max and min
    xmin = self.center.x - self.side /2
    xmax = self.center.x + self.side/2
    ymin = self.center.y - self.side/2
    ymax = self.center.y + self.side/2
    zmin  =self.center.z - self.side/2
    zmax = self.center.z +self.side/2
    return (xmin < p.x <xmax) and (zmin < p.z <zmax) and (ymin < p.y <ymax)

  def is_outside_point(self,p):
    #FIGURE THIS OUT
    xmin = self.center.x - self.side /2
    xmax = self.center.x + self.side/2
    ymin = self.center.y - self.side/2
    ymax = self.center.y + self.side/2
    zmin  =self.center.z - self.side/2
    zmax = self.center.z +self.side/2
    if(p.x < xmin or p.x > xmax or p.y < ymin or p.y > ymax or p.z < zmin or p.z > zmax):
      return False
    else:
      return True

  # determine if a Sphere is strictly inside this Cube
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):

    sphere_mins = a_sphere.get_mins()
    sphere_maxes = a_sphere.get_maxes()

    cube_mins = self.get_mins()
    cube_maxes = self.get_maxes()

    if cube_mins[0] < sphere_mins[0] < sphere_maxes[0] < cube_maxes[0] and \
        cube_mins[1] < sphere_mins[1] < sphere_maxes[1] < cube_maxes[1] and \
        cube_mins[2] < sphere_mins[2] < sphere_maxes[2] < cube_maxes[2]:

        is_inside = True

    else:

        is_inside = False

    return is_inside

  # determine if another Cube is strictly inside this Cube
  # other is a Cube object
  # returns a Boolean
  def is_inside_cube (self, other):
    lst = other.verticies()
    for x in lst:
      if(self.is_inside_point(x) == False):
        return False
    return True

    """dist_center = self.center.distance(other.center)
    return (dist_center + (math.sqrt(3) *other.side)) < math.sqrt(3) * self.side #FIND THE DIAGONAL   """

  # determine if a Cylinder is strictly inside this Cube
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, a_cyl):

      other_maxes = a_cyl.get_maxes()
      other_mins = a_cyl.get_mins()

      self_maxes = self.get_maxes()
      self_mins = self.get_mins()

      # checks to see if cyl's maxes and mins are inside the sphere's maxes and mins
      if self_mins[0] < other_mins[0] < other_maxes[0] < self_maxes[0] and \
              self_mins[1] < other_mins[1] < other_maxes[1] < self_maxes[1] and \
              self_mins[2] < other_mins[2] < other_maxes[2] < self_maxes[2]:

          is_inside = True

      else:

          is_inside = False

      return is_inside

  ''' dist_center = self.center.distance(a_cyl.center)
    return (dist_center - a_cyl.radius) > self.radius '''

  # determine if another Cube intersects this Cube
  # two Cube objects intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, other):
    '''
    if (self.is_inside_cube(other) ==  False) or (self.is_inside_cube(other) ==  True):
          return True
    elif (other.is_inside_cube(self) ==  False) or (other.is_inside_cube(self) ==  True):
          return True
    else:
          return False
    '''
    if self.is_inside_cube(other) == False and \
            other.is_inside_cube(self) == False and \
            Cylinder.is_outside(self, other) == False:

        intersect = True

    else:

        intersect = False

    return intersect

  # determine the volume of intersection if this Cube
  # intersects with another Cube
  # other is a Cube object
  # returns a floating point number
  def intersection_volume (self, other):
    ans = abs((self.x - other.x) * (self.y - other.y) * (self.z - other.z))
    return float(ans)

  # return the largest Sphere object that is inscribed
  # by this Cube
  # Sphere object is inside the Cube and the faces of the
  # Cube are tangential planes of the Sphere
  # returns a Sphere object
  def inscribe_sphere (self):
    radius = self.side/2
    sphere = Sphere(self.center.x, self.center.y, self.center.z, radius)
    return sphere

#---------------------------------------------------------------------------------------

class Cylinder (object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
    self.x = float(x)
    self.y = float(y)
    self.z = float(z)
    self.radius = float(radius)
    self.height = float(height)
    self.center = Point(x,y,z)

  # returns a string representation of a Cylinder of the form:
  # Center: (x, y, z), Radius: value, Height: value
  def __str__ (self):
    return "Center: (" + str(self.x) +", " + str(self.y)+", "  +str(self.z) + ")," + " Radius: " + str(self.radius) + ", " + "Height: " + str(self.height)

  # compute surface area of Cylinder
  # returns a floating point number
  def area (self):
    # 2 * pi * r * h + (pi * r^2)
    return (2 * math.pi * self.radius * self.height) + (2 * math.pi * (self.radius ** 2))

  # compute volume of a Cylinder
  # returns a floating point number
  def volume (self):
    # pi r^2 h
    return math.pi * (self.radius ** 2) * self.height

  def get_maxes(self):

    maxes = []

    maxes.append(self.center.x + self.radius)
    maxes.append(self.center.y + self.radius)
    maxes.append(self.center.z + (self.height/2))

    return maxes

  def get_mins(self):

    mins = []

    mins.append(self.center.x - self.radius)
    mins.append(self.center.y - self.radius)
    mins.append(self.center.z - (self.height / 2))

    return mins

  # determine if a Point is strictly inside this Cylinder
  # p is a Point object
  # returns a Boolean
  def is_inside_point (self, p):

    maxes = self.get_maxes()
    mins = self.get_mins()

    # checks to see if point is inside maxes and mins
    if (mins[0] < p.x < maxes[0]) and \
            (mins[1] < p.y < maxes[1]) and \
            (mins[2] < p.z < maxes[2]):

        is_inside = True

    else:

        is_inside = False

    return is_inside

  # determine if a Sphere is strictly inside this Cylinder
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):

    sphere_maxes = a_sphere.get_maxes()
    sphere_mins = a_sphere.get_mins()

    cyl_maxes = self.get_maxes()
    cyl_mins = self.get_mins()

    if cyl_mins[0] < sphere_mins[0] < sphere_maxes[0] < cyl_maxes[0] and \
        cyl_mins[1] < sphere_mins[1] < sphere_maxes[1] < cyl_maxes[1] and \
        cyl_mins[2] < sphere_mins[2] < sphere_maxes[2] < cyl_maxes[2]:

        is_inside = True

    else:

        is_inside = False

    return is_inside

    # if a_sphere.is_outside_sphere()
    # """lst = self.verticies()
    # for x in lst:
    # if(self.is_inside_point(a_sphere) == True):
    # return True
    # return False """

  # determine if a Cube is strictly inside this Cylinder
  # determine if all eight corners of the Cube are inside
  # the Cylinder
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):

    vert_list = a_cube.get_vertices()

    check_list = []

    for vert in vert_list:

        if self.is_inside_point(vert) == True:
            check_list.append(True)
        else:
            check_list.append(False)

    if False in check_list:

        is_inside = False
    else:

        is_inside = True

    return is_inside


  def is_outside(shape1, shape2):

    maxes1 = shape1.get_maxes()
    mins1 = shape1.get_mins()

    maxes2 = shape2.get_maxes()
    mins2 = shape2.get_mins()

    check_list = []

    # checks if the min x of shape2 is larger than the max x of shape1
    # basically checks if shape2 is outside to the right of shape1
    if maxes1[0] < mins2[0]:
        check_list.append(True)

    # checks if the max x of shape2 is less than the min x of shape1
    # basically checks if shape2 is outside to the left of shape1
    if maxes2[0] < mins1[0]:
        check_list.append(True)

    # checks if the min y of shape2 is larger than the max y of shape1
    # basically checks if shape2 is in front of shape1
    if maxes1[1] < mins2[1]:
        check_list.append(True)

    # checks if the max y of shape2 is less than the min y of shape1
    # basically checks if shape2 is behind shape1
    if maxes2[1] < mins1[1]:
        check_list.append(True)

    # checks if the min z of shape2 is larger than the max z of shape1
    # basically checks if shape2 is above shape1
    if maxes1[2] < mins2[2]:
        check_list.append(True)

    # checks if the max z of shape2 is less than the min z of shape1
    # basically checks if shape2 is below shape1
    if maxes2[2] < mins1[2]:
        check_list.append(True)

    if True in check_list:
        is_outside = True
    else:
        is_outside = False

    return is_outside

  # determine if another Cylinder is strictly inside this Cylinder
  # other is Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, other):

    # gets maxes and mins for the self cylinder
    self_maxes = self.get_maxes()
    self_mins = self.get_mins()

    # gets maxes and mins for the other cylinder
    other_maxes = other.get_maxes()
    other_mins = other.get_mins()

    # checks to see if other cylinder's maxes and mins are inside the self cylinder's maxes and mins
    if self_mins[0] < other_mins[0] < other_maxes[0] < self_maxes[0] and \
            self_mins[1] < other_mins[1] < other_maxes[1] < self_maxes[1] and \
            self_mins[2] < other_mins[2] < other_maxes[2] < self_maxes[2]:

        is_inside = True

    else:

        is_inside = False

    return is_inside

  # determine if another Cylinder intersects this Cylinder
  # two Cylinder object intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cylinder object
  # returns a Boolean
  def does_intersect_cylinder (self, other):

    if self.is_inside_sphere(other) == False and \
            other.is_inside_sphere(self) == False and \
            Cylinder.is_outside(self, other) == False:

        intersect = True

    else:

        intersect = False

    return intersect


  def distance_checker(distP, distQ):

    if distP > distQ:
        msg = 'Distance of Point p from the origin is greater than the distance of Point q from the origin'
        return msg
    else:
        msg = 'Distance of Point p from the origin is not greater than the distance of Point q from the origin'
        return msg

  def sXp_checker(sphereA, P):

      if sphereA.is_inside_point(P) == True:
          msg = 'Point p is inside sphereA'
          return msg
      else:
          msg = 'Point p is not inside sphereA'
          return msg

  def sXs_checker(sphereA, sphereB):

      if sphereA.is_inside_sphere(sphereB) == True:
          msg = 'sphereB is inside sphereA'
          return msg
      else:
          msg = 'sphereB is not inside sphereA'
          return msg

  def sXcube_checker(sphereA, cubeA):

      if sphereA.is_inside_cube(cubeA) == True:
          msg = 'cubeA is inside sphereA'
          return msg
      else:
          msg = 'cubeA is not inside sphereA'
          return msg

  def test_cases():
    origin = Point(0,0,0)
    point1 = Point(0,0,1)
    point2 = Point(0, 1, 0)
    point3 = Point(1, 0, 0)
    point4 = Point(100, 100, 100)

    sphere1 = Sphere(0,0,0,6)
    sphere2 = Sphere(0, 0, 0, 1)
    sphere3 = Sphere(100, 100, 100, 1)
    sphere4 = Sphere(2, 0, 0, 6)

    cube1 = Cube(0, 0, 0, 1)
    cube2 = Cube(100, 100, 100, 1)
    cube3 = Cube(4, 0, 0, 8)
    cube4 = Cube(0, 0, 0, 12)
    cube5 = Cube(6, 0, 0, 12)
    circ_test = Cube(0, 0, 0, 6.92820323028)

    cyl1 = Cylinder(0, 0, 0, 1, 1)
    cyl2 = Cylinder(100, 100, 100, 1, 1)
    cyl3 = Cylinder(3, 0, 0, 6, 1)
    cyl4 = Cylinder(0, 0, 0, 6, 100)
    cyl5 = Cylinder(0, 0, 0, 6, 6)
    cyl6 = Cylinder(3, 0, 0, 6, 6)

    insc_test = cube4.inscribe_sphere()

    tol = 1.0e-6

#---------------------------------------------------------------------------------------

def main():

    # read data from standard input
    coords_list = sys.stdin.readline().split()

    # gets coords for point p
    p = coords_list[0]

    # gets coords for point q
    q = coords_list[1]

    # gets center and radius for sphereA
    sphereA_center = (coords_list[2][0], coords_list[2][1], coords_list[2][2])
    sphereA_radius = coords_list[2][3]

    # gets center and radius for sphereB
    sphereB_center = (coords_list[3][0], coords_list[3][1], coords_list[3][2])
    sphereB_radius = coords_list[3][3]

    # gets center and side for cubeA
    cubeA_center = (coords_list[4][0], coords_list[4][1], coords_list[4][2])
    cubeA_side = coords_list[4][3]

    # gets center and side for cubeB
    cubeB_center = (coords_list[5][0], coords_list[5][1], coords_list[5][2])
    cubeB_side = coords_list[5][3]

    # gets center, radius, and height of cylA
    cylA_center = (coords_list[6][0], coords_list[6][1], coords_list[6][2])
    cylA_radius = coords_list[6][3]
    cylA_height = coords_list[6][4]

    # gets center, radius, and height of cylA
    cylB_center = (coords_list[7][0], coords_list[7][1], coords_list[7][2])
    cylB_radius = coords_list[7][3]
    cylB_height = coords_list[7][4]

    # create a Point object P

    P = Point(p[0], p[1], p[2])

    # create a Point object

    Q = Point(q[0], q[1], q[2])

    # create a Sphere object for sphereA

    sphereA = Sphere(sphereA_center[0], sphereA_center[1], sphereA_center[2], sphereA_radius)


    # create a Sphere object for sphereB

    sphereB = Sphere(sphereB_center[0], sphereB_center[1], sphereB_center[2], sphereB_radius)

    # create a Cube object for cubeA

    cubeA = Cube(cubeA_center[0], cubeA_center[1], cubeA_center[2], cubeA_side)

    # create a Cube object for cubeB

    cubeB = Cube(cubeB_center[0], cubeB_center[1], cubeB_center[2], cubeB_side)

    # create a Cylinder object for cylA

    cylA = Cylinder(cylA_center[0], cylA_center[1], cylA_center[2], cylA_radius, cylA_height)

    # create a Cylinder object

    cylB = Cylinder(cylB_center[0], cylB_center[1], cylB_center[2], cylB_radius, cylB_height)



    # print if the distance of p from the origin is greater
    # than the distance of q from the origin

    #defines the origin
    origin = Point(0,0,0)

    #find the distance between P and origin
    distP = Point.distance(P, origin)

    #find the distance between Q and origin
    distQ = Point.distance(Q, origin)

    #checks which distance is bigger or if they are equal and prints it
    print(Cylinder.distance_checker(distP, distQ))

    #prints blank line
    print()

    # print if Point p is inside sphereA
    print(Cylinder.sXp_checker(sphereA, P))

    # print if sphereB is inside sphereA
    print(Cylinder.sXs_checker(sphereA, sphereB))

    # print if cubeA is inside sphereA
    print(Cylinder.sXcube_checker(sphereA, cubeA))

    # print if cylA is inside sphereA

    if sphereA.is_inside_cyl(cylA) == True:

        print("cylA is inside sphereA")

    else:

        print("cylA is not inside sphereA")


    # print if sphereA intersects with sphereB


    if sphereA.does_intersect_sphere(sphereB) == True:

        print('sphereA does intersect sphereB')

    else:

        print('sphereA does not intersect sphereB')


    # print if cubeB intersects with sphereB


    if sphereB.does_intersect_cube(cubeB) == True:

        print('cubeB does intersect sphereB')

    else:

        print('cubeB does not intersect sphereB')


    # print if the volume of the largest Cube that is circumscribed
    # by sphereA is greater than the volume of cylA

    circ_cube = sphereA.circumscribe_cube()
    circ_cube_volume = circ_cube.volume()
    cylA_volume = cylA.volume()

    if circ_cube_volume > cylA_volume:

        print('Volume of the largest Cube that is circumscribed by sphereA is greater than '
              'the volume of cylA')

    else:

        print('Volume of the largest Cube that is circumscribed by sphereA is not greater than '
              'the volume of cylA')


    #print blank line
    print()

    # print if Point p is inside cubeA

    if cubeA.is_inside_point(P) == True:
        print('Point p is inside cubeA')
    else:
        print('Point p is not inside cubeA')


    # print if sphereA is inside cubeA

    if cubeA.is_inside_sphere(sphereA) == True:
        print('sphereA is inside cubeA')
    else:
        print('sphereA is not inside cubeA')


    # print if cubeB is inside cubeA


    if cubeA.is_inside_cube(cubeB) == True:
        print('cubeB is inside cubeA')
    else:
        print('cubeB is not inside cubeA')

    # print if cylA is inside cubeA


    if cubeA.is_inside_cylinder(cylA) == True:
        print('cylA is inside cubeA')
    else:
        print('cylA is not inside cubeA')

    # print if cubeA intersects with cubeB

    if cubeA.does_intersect_cube(cubeB) == True:
        print('cubeA does intersect cubeB')
    else:
        print('cubeA does not intersect cubeB')


    # print if the intersection volume of cubeA and cubeB
    # is greater than the volume of sphereA

    intersection_volume = cubeA.intersection_volume(cubeB)

    if intersection_volume > sphereA.volume():
        print('Intersection volume of cubeA and cubeB is greater than the volume of sphereA')
    else:
        print('Intersection volume of cubeA and cubeB is not greater than the volume of sphereA')

    # print if the surface area of the largest Sphere object inscribed
    # by cubeA is greater than the surface area of cylA

    sphere = cubeA.inscribe_sphere()

    if sphere.volume() > cylA.area():
        print('Surface area of the largest Sphere object inscribed by cubeA is greater than '
              'the surface area of cylA')
    else:
        print('Surface area of the largest Sphere object inscribed by cubeA is not greater than '
              'the surface area of cylA')

    # prints blank line
    print()

    # print if Point p is inside cylA


    if cylA.is_inside_point(P) == True:
        print('Point p is inside cylA')
    else:
        print('Point p is not inside cylA')


    # print if sphereA is inside cylA

    if cylA.is_inside_sphere(sphereA) == True:
        print('sphereA is inside cylA')
    else:
        print('sphereA is not inside cylA')


    # print if cubeA is inside cylA

    if cylA.is_inside_cube(cubeA) == True:
        print('cubeA is inside cylA')
    else:
        print('cubeA is not inside cylA')

    # print if cylB is inside cylA

    if cylA.is_inside_cylinder(cylB) == True:
        print('cylB is inside cylA')
    else:
        print('cylB is not inside cylA')

    # print if cylB intersects with cylA

    if cylB.does_intersect_cylinder(cylA) == True:
        print('cylB does intersect cylA')
    else:
        print('cylB does not intersect cylA')

    print()
    Cylinder.test_cases()

if __name__ == "__main__":
  main()
