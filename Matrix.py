import numpy
a=numpy.array([[5,6],[8,9]])
b=numpy.array([[10,15],[20,30]])
print ("Addition of two matrices: ")
print (numpy.add(a,b))
print ("Subtraction of two matrices: ")
print (numpy.subtract(a,b))
print ("Division of two marices: ")
print (numpy.divide(a,b))
print ("Multiplication of two matrices: ")
print (numpy.multiply(a,b))
print ("product of two matrices: ")
print (numpy.dot(a,b))
print ("Square root is: ")
print (numpy.sqrt(a))
print ("The addition of elements: ")
print (numpy.add(b))
print ("The colum wise addition: ")
print (numpy.add(b,a=0))
print ("The row wise of addition: ")
print (numpy.add(b,a=1))
print ("Matrix transposition: ")
print (a.T)

