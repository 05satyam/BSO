# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np
# import random
# from functions import *
#
# xvals = np.linspace(2.7, 3.5, 300)
# yvals = []
#
# for i in range(0, 300):
#     yvals.append(2 + xvals[i]**2 - 2*math.cos(2*math.pi*xvals[i]))
# #     xarr.append(x)
# #     yarr.append(y)
# xarr=[]#these arrays are for showing the points in the plot
# yarr=[]
# xarr.append(3.2)
# yarr.append(13.17)
# xarr.append(3.3)
# yarr.append(13.13)
#
# plt.plot(xvals, yvals)    #plotting the points
# plt.plot(xarr, yarr, color='g')    #connecting the points
#
# plt.plot(3.2, 13.17, markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)    #plotting the points
# plt.plot(3.2, 2 + 3.2**2 - 2*math.cos(2*math.pi*3.2), markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)    #plotting the points
#
# plt.plot(3.25, 13.15, markerfacecolor='orange', markeredgecolor='orange', marker='o', markersize=5)
# plt.plot(3.25, 2 + 3.25**2 - 2*math.cos(2*math.pi*3.25), markerfacecolor='orange', markeredgecolor='orange', marker='o', markersize=5)    #plotting the points
#
# xarr=[]#these arrays are for showing the points in the plot
# yarr=[]
# xarr.append(3.25)
# yarr.append(13.15)
# xarr.append(3.3)
# yarr.append(13.13)
# plt.plot(xarr, yarr, color='orange')    #connecting the points
#
# plt.plot(3.3, 13.13, markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)    #plotting the points
# plt.plot(3.3, 2 + 3.3**2 - 2*math.cos(2*math.pi*3.3), markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)    #plotting the points
# plt.show()
#
# plt.plot(xvals, yvals)    #plotting the points
# plt.plot(xarr, yarr, color='g')    #connecting the points
#
# plt.plot(3.25, 13.15, markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)
# plt.plot(3.25, 2 + 3.25**2 - 2*math.cos(2*math.pi*3.25), markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)    #plotting the points
#
# plt.plot(3.3, 13.13, markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)    #plotting the points
# plt.plot(3.3, 2 + 3.3**2 - 2*math.cos(2*math.pi*3.3), markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)    #plotting the points
# plt.show()
#
# plt.plot(xvals, yvals)    #plotting the points
#
# plt.plot(3.275, 13.14, markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)
# # plt.plot(3.275, 2 + 3.275**2 - 2*math.cos(2*math.pi*3.275), markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)    #plotting the points
# plt.show()

#load modules/libraries
import turtle
import math

'''
class solar system with 
   const: __init__
   
   attributes/class variables realted to solar system: 
    self.__theSun = None
    self.__planets = []
    self.__ssTurtle = turtle.Turtle()
    self.__ssTurtle.hideturtle()
    self.__ssScreen = turtle.Screen()
    self.__ssScreen.setworldcoordinates (-width/2.0,-height/2.0,width/2.0, height/2.0)
    
    class methods/behaviors
      mutators:
       def addPlanet(self, aPlanet):
         self.__planets.append(aPlanet)
    
      def addSun(self, aSun):
        self.__theSun = aSun
        
      
    
  
'''
class SolarSystem:
  def __init__(self, width, height):
    self.__theSun = None
    self.__planets = []     # creating list for storing planets in solar system
    self.__ssTurtle = turtle.Turtle()
    self.__ssTurtle.hideturtle()
    self.__ssScreen = turtle.Screen()
    self.__ssScreen.setworldcoordinates (-width/2.0,-height/2.0,width/2.0, height/2.0)
  def addPlanet(self, aPlanet):  # adding plantes to solar system
    self.__planets.append(aPlanet)
  def addSun(self, aSun):    # adding sun to solar system
    self.__theSun = aSun
  def showPlanets(self):
    for aPlanet in self.__planets:
      print(aPlanet)
  def freeze(self):
    self.__ssScreen.exitonclick()

  def movePlanets(self):  # method to move planets in solar system applyed to all the planets
    G = .1
    dt = .001
    for p in self.__planets: # (item based for loop)loop on planets and move each planet one by one
      p.moveTo(p.getXPos() + dt * p.getXVel(), p.getYPos() + dt * p.getYVel())
      rX = self.__theSun.getXPos() - p.getXPos()
      rY = self.__theSun.getYPos() - p.getYPos()
      r = math.sqrt(rX**2 + rY**2)
      accX = G * self.__theSun.getMass() * rX/r**3
      accY = G * self.__theSun.getMass() * rY/r**3
      p.setXVel(p.getXVel() + dt * accX)
      p.setYVel(p.getYVel() + dt * accY)


'''
class sun
constructor: __init__
attributes/variables: 
    self.name = iname
    self.radius = irad
    self.mass = im
    self.temp = itemp
    self.x = 0
    self.y = 0
    self.sturtle = turtle.Turtle()
    self.sturtle.shape("circle")
    self.sturtle.color("yellow")
    
 method:
    accessors-to access sun class variables:
         def getXPos(self):
          return self.x
        def getYPos(self):
           return self.y
        def getMass(self):
           return self.mass
'''
class Sun:
  def __init__(self, iname, irad, im, itemp):
    self.name = iname
    self.radius = irad
    self.mass = im
    self.temp = itemp
    self.x = 0
    self.y = 0
    self.sturtle = turtle.Turtle()   # creating turtle for sun
    self.sturtle.shape("circle")
    self.sturtle.color("yellow")
    #other methods as before
  def getXPos(self):
    return self.x
  def getYPos(self):
     return self.y
  def getMass(self):
     return self.mass


'''
class planet
contructor:__init__
attributes that define a plante:
     self.__name = iName
      self.__radius = iRad
      self.__mass = iM
      self.__distance = iDist
      self.__x = self.__distance
      self.__y = 0
      self.__velX = iVx
      self.__velY = iVy

      self.__color = iC
      self.__pTurtle = turtle.Turtle()
      self.__pTurtle.color(self.__color)
      self.__pTurtle.shape("circle")
      self.__pTurtle.up()
      self.__pTurtle.goto(self.__x, self.__y)
      self.__pTurtle.down()
      
accessors:
    def getXPos(self):
      return self.__x
    def getYPos(self):
      return self.__y
    def moveTo(self, newX, newY):
      self.__x = newX
      self.__y = newY
      self.__pTurtle.goto(self.__x, self.__y)
    def getXVel(self):
      return self.__velX
    def getYVel(self):
      return self.__velY

mutators:
    def setXVel(self, newVx):
      self.__velX = newVx
    def setYVel(self, newVy):
      self.__velY = newVy
'''
class Planet:
    def __init__(self, iName, iRad, iM, iDist, iC, iVx, iVy):
      self.__name = iName
      self.__radius = iRad
      self.__mass = iM
      self.__distance = iDist
      self.__x = self.__distance
      self.__y = 0
      self.__velX = iVx
      self.__velY = iVy

      self.__color = iC
      self.__pTurtle = turtle.Turtle()
      self.__pTurtle.color(self.__color)
      self.__pTurtle.shape("circle")
      self.__pTurtle.up()
      self.__pTurtle.goto(self.__x, self.__y)
      self.__pTurtle.down()
  #other methods as before
    def getXPos(self):
      return self.__x
    def getYPos(self):
      return self.__y
    def moveTo(self, newX, newY):
      self.__x = newX
      self.__y = newY
      self.__pTurtle.goto(self.__x, self.__y)
    def getXVel(self):
      return self.__velX
    def getYVel(self):
      return self.__velY
    def setXVel(self, newVx):
      self.__velX = newVx
    def setYVel(self, newVy):
      self.__velY = newVy


'''
main method outside all classes to create animation
'''
def createSSandAnimate():
  ss = SolarSystem(2, 2)  # object of solar system
  sun = Sun("Sun", 5000, 10, 5800)  # object of sun
  ss.addSun(sun)  # add sun to solar system
  m = Planet("Mercury", 19.5, 1000,.25, 'blue', 0, 2 )  # create Mercury plant object
  ss.addPlanet(m) #add planet to solar system
  m = Planet("Earth", 47.5, 5000, 0.3,'green', 0, 2.0) # create Earth plant object
  ss.addPlanet(m)#add planet to solar system
  m = Planet("Mars", 50, 9000, 0.5,  'red',0, 1.63) # create Mars plant object
  ss.addPlanet(m)#add planet to solar system
  m = Planet("Jupiter", 100, 49000,  0.7, 'black',0, 1) # create Jupiter plant object
  ss.addPlanet(m)#add planet to solar system
  numTimePeriods = 2000
  for aMove in range(numTimePeriods): # move plantes for 2000 time
    ss.movePlanets()


createSSandAnimate() # call of main method to start the animation