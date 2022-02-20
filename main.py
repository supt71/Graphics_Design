"""
Making an interactive program to make a meadow of unique flowers

Sajid Kamal
CS21
October, 2021

"""


from graphics import *
from random import choice

def makeGrass(win):
    """
    Purpose: to make half of the window grassy
    Parameters: window -- the size of the output window (100X100)
    Return: none
    """
    grass = Rectangle(Point(0,0), Point(100,50))
    grass.setFill("lawn green")
    grass.setOutline("lawn green")

    grass.draw(win)


def makeBorder(win):
    """
    Purpose: to make the closing border at the bottom of the window
    Parameters: window -- the size of the output window (100X100)
    Return: none
    """

    border = Rectangle(Point(0,0), Point(100, 5))
    border.setFill("Black")
    border.draw(win)




def makeDistantFlower(win, f_list):

    """
    Purpose: To make distant flowers darker, and closer flowers lighter
    Parameters: window -- the size of the output window (100X100)
    Return: none
    """

    #flower_list = [outer_blossom, inner_blossom, drawStem, leaf1, leaf2]

    #darkRed = (162,42,42)
    #darkOrange = (220,88,42)
    #lightRed = (255,127,127)
    #darkGolden = (238, 188, 29)
    #lemonYellow = (255, 244, 79)

    out_blossom = f_list[0]
    in_blossom = f_list[1]

    findp2 = f_list[2].getP2()
    finDy = findp2.getY()

    if finDy <30:
        out_blossom.setFill(color_rgb(255,244,79))
        in_blossom.setFill(color_rgb(255,127,127))
    else:
        out_blossom.setFill(color_rgb(238, 188, 29))
        in_blossom.setFill(color_rgb(162,42,42))





def makeCloudyFlower(win, f_list):
    """
    Purpose: to make the unrooted flowers disappear
    Parameters: window -- the size of the output window (100X100)
    Return: none
    """
    #flower_list = [outer_blossom, inner_blossom, drawStem, leaf1, leaf2]

    findP2 = f_list[2].getP2()
    findY = findP2.getY()

    if findY > 50:

        f_list[0].undraw()
        f_list[1].undraw()
        f_list[2].undraw()
        f_list[3].undraw()
        f_list[4].undraw()

        findY = findP2.getY()


def makeBigLittleFlower(win,click1):

    """
    Purpose: to make the random flowers wth random radius
    Parameters: window ---the size of the output window (100X100)
                click1 -- takes the user input from the main function
    Return: none
    """

    rad = win.getWidth()*0.005
    rad_list = [(rad+2),(rad+1), (rad+0.5), (rad+1.5)]
    rad1 = choice(rad_list)


    outer_blossom = Circle(click1, rad1)
    outer_blossom.draw(win)


    center2 = outer_blossom.getCenter()
    rad_2_list = [2,1.5,2.5,1]
    rad2 = choice(rad_2_list)


    inner_blossom = Circle(center2, rad2)
    inner_blossom.draw(win)


    click2 = win.getMouse()
    drawStem = Line(click1, click2)
    drawStem.draw(win)


    #outer_blossom.draw(win)
    #inner_blossom.draw(win)


    centerStem = drawStem.getCenter()
    x1= centerStem.getX()
    x2 = centerStem.getY()
    x3 = centerStem.getX() +4
    x4 = centerStem.getY() +2
    x5 = centerStem.getX() -4
    x6 = centerStem.getY() -2


    leaf1 = Oval(Point(x1,x2), Point(x3,x4))
    leaf1.setFill("green")
    leaf1.draw(win)


    leaf2 = Oval(Point(x1,x2), Point(x5,x6))
    leaf2.setFill("green")
    leaf2.draw(win)

    flower_list = [outer_blossom, inner_blossom, drawStem, leaf1, leaf2]

    return flower_list




def main():

    window = GraphWin("Spring Meadow", 600,600)
    window.setBackground("deep sky blue")
    window.setCoords(0,0,100,100)


#some artistic addition
    makeSun = Circle(Point(73,84),10)
    makeSun.draw(window)
    makeSun.setFill("yellow")
    makeSun.setOutline("yellow")
    makeCloud = Oval(Point(65,75), Point(90,85))
    makeCloud.setFill("white")
    makeCloud.setOutline("white")
    makeCloud.draw(window)
    makeCloud2 = Oval(Point(70,75), Point(90,90))
    makeCloud2.setFill("white")
    makeCloud2.setOutline("white")
    makeCloud2.draw(window)
    makeCloud3 = Oval(Point(80,75), Point(95,88))
    makeCloud3.setFill("white")
    makeCloud3.setOutline("white")
    makeCloud3.draw(window)


    makeGrass(window)
    makeBorder(window)
    userClick = window.getMouse()
    x2 = userClick.getY()


    while x2 > 5:


        f_list = makeBigLittleFlower(window, userClick)
        makeDistantFlower(window, f_list)
        makeCloudyFlower(window, f_list)
        userClick = window.getMouse()

        x2 = userClick.getY()



    window.close()





main()
