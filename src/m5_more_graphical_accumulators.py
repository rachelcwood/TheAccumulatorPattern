"""
This module lets you practice one form of the ACCUMULATOR pattern,
namely, the "IN GRAPHICS" form which features:
  -- DRAWING OBJECTS via ACCUMULATING positions and/or sizes,
     as in:   x = x + pixels

Additionally, it emphasizes that you must
  ** DO A CONCRETE EXAMPLE BY HAND **
before you can implement a solution to the problem in Python. 
  
Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Rachel Wood.
"""  # DONE 1

import rosegraphics as rg


# ----------------------------------------------------------------------
# Students: As you work each of these problems, ask yourself:
#   1. Do I need a loop?
#      If so, HOW MANY LOOPS?
#
#   2. Where I need a loop, what needs to happen:
#        -- BEFORE the loop?
#        -- IN the loop?
#        -- AFTER the loop?
# ----------------------------------------------------------------------
def main():
    """ Calls the   TEST   functions in this module. """
    run_test_draw_squares_from_circle()
    run_test_draw_circles_from_rectangle()
    run_test_draw_lines_from_rectangles()


def run_test_draw_squares_from_circle():
    """ Tests the   draw_squares_from_circle  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  draw_squares_from_circle  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # ------------------------------------------------------------------
    # TWO tests on ONE window.
    # ------------------------------------------------------------------
    title = 'Tests 1 and 2 of DRAW_SQUARES_FROM_CIRCLE: '
    title = title + ' 7 little squares from green circle, 4 big squares'
    window1 = rg.RoseWindow(650, 350, title)

    # Test 1:
    circle = rg.Circle(rg.Point(100, 100), 20)
    circle.fill_color = 'green'
    draw_squares_from_circle(7, circle, window1)

    # Test 2:
    circle = rg.Circle(rg.Point(350, 70), 50)
    draw_squares_from_circle(4, circle, window1)
    window1.close_on_mouse_click()

    # ------------------------------------------------------------------
    # A third test on ANOTHER window.
    # ------------------------------------------------------------------
    title = 'Test 3 of DRAW_SQUARES_FROM_CIRCLE: '
    title += ' 20 teeny squares from blue circle!'
    window2 = rg.RoseWindow(525, 300, title)

    # Test 3:
    circle = rg.Circle(rg.Point(50, 50), 10)
    circle.fill_color = 'blue'
    draw_squares_from_circle(20, circle, window2)

    window2.close_on_mouse_click()


def draw_squares_from_circle(n, circle, window):
    """
    What comes in:  Three arguments:
      -- A positive integer n.
      -- An rg.Circle.
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      See   draw_squares_from_circle.pdf   in this project for pictures
        that may help you better understand the following specification:

      First draws the given rg.Circle on the given rg.RoseWindow.
      Then draws  n  rg.Squares on the given rg.RoseWindow, such that:
        -- The first rg.Square circumscribes the given rg.Circle.
        -- Each subsequent rg.Square has its upper-left quarter
             on top of the lower-right quarter of the previous rg.Square,
             so that the squares form an overlapping sequence
             that goes down and to the right.
      Must  ** render **     but   ** NOT close **   the window.

    Type hints:
      :type n: int
      :type circle: rg.Circle
      :type window: rg.RoseWindow
    """
    # ------------------------------------------------------------------
    # DONE 2
    #          Tests have been written for you (above).
    #
    # CONSIDER using the ACCUMULATOR IN GRAPHICS pattern,
    #             as in   draw_row_of_circles   in m1e,
    #             instead of directly using the loop variable.
    #
    ####################################################################
    # HINT: To figure out the code that computes the necessary
    #       positions of each square,
    #          ** FIRST DO A CONCRETE EXAMPLE BY HAND! **
    ####################################################################
    # ------------------------------------------------------------------
    radius = circle.radius

    circle.attach_to(window)

    x = circle.center.x  # Initialize x and y BEFORE the loop
    y = circle.center.y  # Choose values that make the FIRST object easy to
    # draw

    for _ in range(n):  # Loop that does NOT use its index variable

        square = rg.Square(rg.Point(x, y), radius*2)

        # Attach the object(s) to the window.
        square.attach_to(window)

        # --------------------------------------------------------------
        # Increment x (and in other problems, other variables)
        # for the thing(s) to draw in the NEXT iteration of the loop.
        # --------------------------------------------------------------
        x = x + radius
        y = y + radius

    window.render()


def run_test_draw_circles_from_rectangle():
    """ Tests the   draw_circles_from_rectangle  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  draw_circles_from_rectangle  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # ------------------------------------------------------------------
    # DONE 3
    #   It TESTS the  draw_circles_from_rectangle  function
    #   defined below.  Include at least **   3   ** tests, of which
    #      ***  at least TWO tests are on ONE window and
    #      ***  at least ONE test is on a DIFFERENT window.
    #
    ####################################################################
    # HINT: Consider using the same test cases as suggested by the
    #   pictures in  draw_circles_from_rectangle.pdf   in this project.
    #   Follow the same form as the example in a previous problem.
    ####################################################################
    # ------------------------------------------------------------------
    window1 = rg.RoseWindow(720, 500)

    # Test 1:
    rectangle = rg.Rectangle(rg.Point(400, 250), rg.Point(440, 325))
    rectangle.fill_color = 'green'
    rectangle.outline_thickness = 5
    draw_circles_from_rectangle(4, 5, rectangle, window1)

    # Test 2:
    rectangle = rg.Rectangle(rg.Point(600, 400), rg.Point(500, 450))
    rectangle.fill_color = 'blue'
    rectangle.outline_color = 'red'
    rectangle.outline_thickness = 3
    draw_circles_from_rectangle(8, 3, rectangle, window1)

    # Test 3:
    rectangle = rg.Rectangle(rg.Point(200, 200), rg.Point(270, 150))
    rectangle.fill_color = 'yellow'
    rectangle.outline_color = 'purple'
    rectangle.outline_thickness = 3
    draw_circles_from_rectangle(4, 2, rectangle, window1)

    window1.close_on_mouse_click()

    window1 = rg.RoseWindow(620, 380)

    rectangle = rg.Rectangle(rg.Point(375, 330), rg.Point(350, 280))
    rectangle.fill_color = 'yellow'
    rectangle.outline_color = 'brown'
    rectangle.outline_thickness = 5
    draw_circles_from_rectangle(6, 10, rectangle, window1)

    window1.close_on_mouse_click()


def draw_circles_from_rectangle(m, n, rectangle, window):
    """
    What comes in:  Four arguments:
      -- Positive integers m and n.
      -- An rg.Rectangle.
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      See   draw_circles_from_rectangle.pdf   in this project for pictures
        that may help you better understand the following specification:

      First draws the given rg.Rectangle on the given rg.RoseWindow.
      Then draws  m  rg.Circles on the given rg.RoseWindow, such that:
        -- The diameter of each rg.Circle is the same as the height
             of the given rg.Rectangle.
        -- The first rg.Circle is immediately to the left of the
             given rg.Rectangle
        -- Each subsequent rg.Circle is immediately to the left
             of the previous rg.Circle, so that the circles form a row
             that goes to the left.
        -- Each rg. Circle has the same fill_color as the given
             rg.Rectangle (and has no outline_color).
      Then draws  n  rg.Circles on the given RoseWindow, such that:
        -- The diameter of each rg.Circle is the same as the width
             of the given rg.Rectangle.
        -- The first rg.Circle is immediately above the
             given rg.Rectangle
        -- Each subsequent rg.Circle is immediately above the previous
             rg.Circle, so that the circles form a column that goes up.
        -- Each rg.Circle has the same outline_color as the given
             rg.Rectangle (and has no fill_color).
      Must  ** render **     but   ** NOT close **   the window.

    Type hints:
      :type m: int
      :type n: int
      :type rectangle: rg.Rectangle
      :type window: rg.RoseWindow
    """
    # ------------------------------------------------------------------
    # DONE 4
    #          Tests have been written for you (above).
    #
    # CONSIDER using the ACCUMULATOR IN GRAPHICS pattern,
    #             as in   draw_row_of_circles   in m1e,
    #             instead of directly using the loop variable.
    #
    ####################################################################
    # HINT: To figure out the code that computes the necessary
    #       positions of each circle,
    #          ** FIRST DO A CONCRETE EXAMPLE BY HAND! **
    ####################################################################
    # ------------------------------------------------------------------
    rectangle.attach_to(window)

    c1x = rectangle.corner_1.x
    c1y = rectangle.corner_1.y
    c2x = rectangle.corner_2.x
    c2y = rectangle.corner_2.y

    if c1x > c2x:
        c1x = rectangle.corner_2.x
        c2x = rectangle.corner_1.x

    if c1y > c2y:
        c1y = rectangle.corner_2.y
        c2y = rectangle.corner_1.y

    r1 = (c2y-c1y)/2
    r2 = (c2x-c1x)/2

    for _ in range(m):
        circle = rg.Circle(rg.Point(c1x-r1, c1y+r1), r1)
        circle.fill_color = rectangle.fill_color

        c1x = c1x - 2*r1

        circle.attach_to(window)

    window.render()

    c1x = rectangle.corner_1.x
    c1y = rectangle.corner_1.y
    c2x = rectangle.corner_2.x
    c2y = rectangle.corner_2.y

    if c1x > c2x:
        c1x = rectangle.corner_2.x
        c2x = rectangle.corner_1.x

    if c1y > c2y:
        c1y = rectangle.corner_2.y
        c2y = rectangle.corner_1.y

    r1 = (c2y - c1y) / 2
    r2 = (c2x - c1x) / 2

    for _ in range(n):
        circle = rg.Circle(rg.Point(c1x+r2, c1y-r2), r2)
        circle.outline_color = rectangle.outline_color

        c1y = c1y - 2*r2

        circle.attach_to(window)

    window.render()


def run_test_draw_lines_from_rectangles():
    """ Tests the   draw_lines_from_rectangles  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  draw_lines_from_rectangles  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # TWO tests on ONE window.
    title = 'Tests 1 & 2 of DRAW_LINES_FROM_RECTANGLES:'
    title += '  5 lines, 8 lines!'
    window1 = rg.RoseWindow(900, 400, title)

    rectangle1 = rg.Rectangle(rg.Point(100, 25), rg.Point(150, 125))
    rectangle2 = rg.Rectangle(rg.Point(300, 150), rg.Point(400, 175))
    rectangle1.outline_color = 'red'
    rectangle2.outline_color = 'blue'
    draw_lines_from_rectangles(rectangle1, rectangle2, 5, window1)

    rectangle1 = rg.Rectangle(rg.Point(870, 30), rg.Point(750, 100))
    rectangle2 = rg.Rectangle(rg.Point(700, 90), rg.Point(650, 60))
    rectangle2.outline_color = 'green'
    draw_lines_from_rectangles(rectangle1, rectangle2, 8, window1)

    window1.close_on_mouse_click()

    # A third test on ANOTHER window.
    title = 'Test 3 of DRAW_LINES_FROM_RECTANGLES:  11 lines!'
    window2 = rg.RoseWindow(700, 700, title)

    rectangle1 = rg.Rectangle(rg.Point(550, 200), rg.Point(650, 100))
    rectangle2 = rg.Rectangle(rg.Point(600, 50), rg.Point(650, 75))
    rectangle1.outline_color = 'brown'
    rectangle2.outline_color = 'cyan'
    rectangle2.outline_thickness = 10
    draw_lines_from_rectangles(rectangle1, rectangle2, 11, window2)

    window2.close_on_mouse_click()


def draw_lines_from_rectangles(rectangle1, rectangle2, n, window):
    """
    What comes in:  Four arguments:
      -- Two rg.Rectangles.
      -- A positive integer n.
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      See   draw_lines_from_rectangles.pdf   in this project
      for pictures that may help you better understand
      the following specification:

      First draws the given rg.Rectangles on the given rg.RoseWindow.
      Then draws  n  rg.Lines on the given rg.RoseWindow, such that:
        -- The 1st rg.Line goes from the center of one of the
             1st rg.Rectangle to the center of the 2nd rg.Rectangle.
        -- The 2nd rg.Line goes from the lower-left corner of the
              1st rg.Rectangle and is parallel to the 1st rg.Line,
              with the same length and direction as the 1st rg.Line.
        -- Subsequent rg.Lines are shifted from the previous rg.Line in
              the same way that the 2nd rg.Line is shifted from the 1st.
        -- Each of the rg.Lines has thickness 5.
        -- The colors of the rg.Lines alternate, as follows:
             - The 1st, 3rd, 5th, ... rg.Line has color R1_color
             - The 2nd, 4th, 6th, ... rg.Line has color R2_color
            where
             - R1_color is the outline color of the 1st rg.Rectangle
             - R2_color is the outline color of the 2nd rg.Rectangle
      Must  ** render **     but   ** NOT close **   the window.

    Type hints:
      :type rectangle1: rg.Rectangle
      :type rectangle2: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
      """
    # ------------------------------------------------------------------
    # DONE 5
    #          Tests have been written for you (above).
    #
    # CONSIDER using the ACCUMULATOR IN GRAPHICS pattern,
    #             as in   draw_row_of_circles   in m1e,
    #             instead of directly using the loop variable.
    #
    ####################################################################
    # HINT: To figure out the code that computes the necessary
    #       endpoints for each line,
    #          ** FIRST DO A CONCRETE EXAMPLE BY HAND! **
    ####################################################################
    # ------------------------------------------------------------------
    rectangle1.attach_to(window)
    rectangle2.attach_to(window)

    c1x1 = rectangle1.corner_1.x
    c1y1 = rectangle1.corner_1.y
    c2x1 = rectangle1.corner_2.x
    c2y1 = rectangle1.corner_2.y

    if c1x1 < c2x1:
        c1x1 = rectangle1.corner_2.x
        c2x1 = rectangle1.corner_1.x

    if c1y1 < c2y1:
        c1y1 = rectangle1.corner_2.y
        c2y1 = rectangle1.corner_1.y

    L1_1 = (c1y1 - c2y1)/2
    L2_1 = (c1x1 - c2x1)/2

    c1x2 = rectangle2.corner_1.x
    c1y2 = rectangle2.corner_1.y
    c2x2 = rectangle2.corner_2.x
    c2y2 = rectangle2.corner_2.y

    if c1x2 < c2x2:
        c1x2 = rectangle2.corner_2.x
        c2x2 = rectangle2.corner_1.x

    if c1y2 < c2y2:
        c1y2 = rectangle2.corner_2.y
        c2y2 = rectangle2.corner_1.y

    L1_2 = (c1y2 - c2y2)/2
    L2_2 = (c1x2 - c2x2)/2

    #print(L2_1)
    #print(L2_1+c1x1)

    pointone = rg.Point(L2_1+c2x1, L1_1+c2y1)
    pointtwo = rg.Point(L2_2+c2x2, L1_2+c2y2)

    line = rg.Line(pointone, pointtwo)
    line.color = rectangle1.outline_color
    line.thickness = 5

    line.attach_to(window)

    for k in range(n-1):
        pointone = rg.Point(pointone.x - L2_1, pointone.y + L1_1)
        pointtwo = rg.Point(pointtwo.x - L2_1, pointtwo.y + L1_1)

        # print(pointone)
        # print(pointtwo)

        line = rg.Line(pointone, pointtwo)
        if (k+2) % 2 == 0:
            line.color = rectangle2.outline_color
        else:
            line.color = rectangle1.outline_color

        line.thickness = 5

        line.attach_to(window)

    window.render()
    # Note to self. Make sure to check the inequalities to get the desiered
    # answers


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
