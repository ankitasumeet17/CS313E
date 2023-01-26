#  File: Poly.py

#  Description: Linked List Representation of Polynomials

#  Student Name: Ankita Sumeet 

#  Student UT EID: as96977

#  Partner Name: Jingwen (Ivy) Lou

#  Partner UT EID: --

#  Course Name: CS 313E

#  Unique Number: A17

#  Date Created: 11/7/21

#  Date Last Modified: 11/8/21

import sys

class Link (object):
    def __init__ (self, coeff = 1, exp = 1, next = None):
        self.coeff = coeff
        self.exp = exp
        self.next = next

    def __str__ (self):
        return '(' + str (self.coeff) + ', ' + str (self.exp) + ')'

class LinkedList (object):
    def __init__ (self, head = None, tail = None):
        self.first = None
        self.head =  head
        self.tail - tail
        self.length = 0

    # keep Links in descending order of exponents
    def insert_in_order (self, coeff, exp):
        self.length += 1
        new = Link(coeff, exp)
        if(self.head == None):
            self.head = self.tail = new
        else:
            prev = current = self.head
            while current.exp >= exp:
                prev = current
                current = current.next
                if current == None:
                    prev.next = new
                    self.tail = new
                    return
            if current == self.head:
                new.next = current
                self.head = new
            else:
                prev.next = new
                new.next = current

    # add polynomial p to this polynomial and return the sum
    def add (self, p):
        if self.head == None:
            return p
        elif p.head == None:
            return self
        else:
            sumLst = LinkedList()
            polySelf = self.head
            polyOther = p.head
            # combine 
            while polySelf != None and polyOther != None:
                if(polySelf.exp == polyOther.exp):
                    sumLst.insert_in_order((polySelf.coeff + polyOther.coeff), polySelf.exp)
                    polySelf = polySelf.next
                    polyOther = polyOther.next
                elif polySelf.exp > polyOther.exp:
                    sumLst.insert_in_order(polySelf.coeff, polySelf.exp)
                    polySelf = polySelf.next
                else:
                    sumLst.insert_in_order(polyOther.coeff, polyOther.exp)
                    polyOther = polyOther.next            
            # check remaining
            while polySelf != None:
                sumLst.insert_in_order(polySelf.coeff, polySelf.exp)
                polySelf = polySelf.next
            while polyOther != None:
                sumLst.insert_in_order(polyOther.coeff, polyOther.exp)
                polyOther = polyOther.next 
            return sumLst

    # multiply polynomial p to this polynomial and return the product
    def mult (self, p):
        if self.head == None:
            return p
        elif p.head == None:
            return(self)
        else:
            productLst = LinkedList()
            polySelf = self.head
            while(polySelf != None):
                polyOther = p.head
                while(polyOther != None):
                    nCoeff = polySelf.coeff * polyOther.coeff
                    nExp = polySelf.exp + polyOther.exp
                    productLst.insert_in_order(nCoeff, nExp)
                    polyOther = polyOther.next
                polySelf = polySelf.next
            return(productLst)

    # create a string representation of the polynomial
    def __str__ (self):
        if self.head == None:
            return ""
        curr = self.head
        polyStr = f"{curr}"
        while curr.next != None:
            curr = curr.next
            polyStr += f" + {curr}"
        return polyStr

def main():
    # read data from file poly.in from stdin
    line = sys.stdin.readline()
    line = line.strip()
    num_points = int (line)
    
    # create polynomial p

    # create polynomial q

    # get sum of p and q and print sum
    sumLst = p.add(q)
    print(f"Sum: {sumLst}\n")

    # get product of p and q and print product
    prodLst = p.mult(q)
    prodLst.simplify()
    print(f"Product: {prodLst}")

if __name__ == "__main__":
  main()
