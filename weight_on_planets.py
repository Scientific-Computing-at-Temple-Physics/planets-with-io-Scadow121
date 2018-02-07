# This is a comment.  Python will ignore these lines (starting with #) when running

import math as ma
from scipy.constants import G
import sys
# To use a math function, write "ma." in front of it.  Example:  ma.sin(3.146)

#To Do:






#open, sort, and format planet data
data = open("planet_data.dat", "r")
p=[]
for line in data:
    x=line.split(';')
    x=[a.strip('g/cm^3') for a in x]
    x=[a.strip('\n') for a in x]
    x=[a.strip('\t') for a in x]
    x=[a.strip('km') for a in x]
    x=[a.strip(' ') for a in x]
#    print x
    if len(x) >1:
        p=p+x
    else: continue
#print p

#prompt and format user inputs
planet=raw_input('Body of Interest: ')
altitude=raw_input('Altitude of Explorer in Meters: ')
mass=raw_input('Mass of Explorer in Kilograms: ')
if altitude.isdigit == True:
    altitude=float(altitude)
else:
    print 'Invalid Input for Altitude'
    sys.exit()
if mass.isdigit == True:
    mass=float(mass)
else:
    print 'Invalid Input for Mass'
    sys.exit()

#figure out which data to use
n1=0
info=None
while n1 < len(p):
    if p [n1] == planet:
        info=p [n1:n1+3]
#        print info
        n1=len(p)+1
    else: n1=n1+4

if info is None:
    print ''
    print 'Invalid Input for Body'
else:
    prad=float(info [1])*1000
    pden=float(info [2])*1000
    #print prad
    #print pden

    #math stuff
    v=(4.0/3.0)*ma.pi*(prad**3)
    #print v
    m=v*pden
    #print m
    f=G*((mass*m)/((altitude+prad)**2))
    a=f/(mass)
    print ''
    print "The explorer currently weighs", f, "Newtons and is experiencing a gravitational acceleration of", a, "Meters per Second squared.  "
