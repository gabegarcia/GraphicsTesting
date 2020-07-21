from graphics import *

def main():
  win = GraphWin('Shapes')
    
  center = Point(100, 100)
  circ = Circle(center, 30)
  circ.setFill(color_rgb(130, 0, 103))
  circ.draw(win)

  
  rect = Rectangle(Point(30, 30), Point(70, 70))
  rect.setFill('blue')
  win.getMouse()
  rect.draw(win)

  win.getMouse()
  rect = Rectangle(Point(100, 100), Point(170, 170))
  rect.setFill('green')
  rect.draw(win)

  win.getMouse()
  win.close()

main()