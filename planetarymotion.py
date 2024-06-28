# USEFUL MATH FUNCTIONS
from math import sin, cos, sqrt

# THE FUNDAMENTAL CONSTANT
from math import pi

# THE GRAPHICS PACKAGE
import turtle

##############################################################################

# SIMULATION PARAMETERS
YR = 365.25     # How many days in one year?
AU = 50         # How many pixels define one astronomical unit?
TIME = 1.0*YR   # How many days to run the simulation?
STEP = 10       # How many days between each graphics update?

##############################################################################

# DEFINE SOME REUSABLE FUNCTIONS

""" Distance from the origin to either focal point of the ellipse. """
def ellipse_focus(a, e):
    # TODO: Change this for #3.
    return 0

""" Total time for a planet to complete one orbit around the Sun. """
def ellipse_period(a, e):
    # TODO: Change this for #9.
    return YR

""" Distance from the origin to the nearest point on the ellipse. """
def ellipse_semiminoraxis(a, e):
    return a * sqrt(1 - e**2)

""" Fraction of a planet's progress around its orbit after t days. """
def ellipse_fraction(a, e, t):
    T = ellipse_period(a,e) if a != 0 else 1.0
    # NOTE: The if/else statement avoids division by zero when a=0 (as for Sol).
    return t/T

""" Calculate the (x,y) coordinate of a planet after t days. """
def ellipse_coordinates(a, e, t):
    # COMPUTE DERIVED VALUES
    b = ellipse_semiminoraxis(a, e)
    c = ellipse_focus(a, e)
    chi = ellipse_fraction(a, e, t)

    # STANDARD DEFINITION OF AN ELLIPSE
    x = a * cos(2*pi * chi) - c
    y = b * sin(2*pi * chi)

    # NOTE: The standard is to put the semimajor axis along the x-axis,
    #   but the simulation shows it vertically.
    # Therefore, we compute the ordered pair backwards, as (y,x).
    return y, x

""" Initialize a pen and bundle related quantities into a "planet" dict.

Parameters
----------
- `name` <str>: The name of the planet, which will be printed as a label.
- `a` <int>: The semimajor axis of the planet's orbit.
- `e` <int>: The eccentricity of the planet's orbit.
- `color` <string>: The name of the color to use for the planet.

Returns
-------
A dict with the following attributes:
- "pen": the `turtle.Turtle` object, initialized with the appropriate color
- "a": the semimajor axis of the planet's orbit
- "e": the eccentricity of the planet's orbit
- "name": the name of the planet

"""
def make_planet(name="", a=AU, e=0.0, color="black"):
    # CREATE THE PEN OBJECT
    pen = turtle.Turtle()

    # SET THE INITIAL STATE OF THE PEN
    pen.hideturtle()    # Pen starts invisible.
    pen.up()            # Pen does not draw, until is put "down".
    pen.speed(0)        # Pen does not have any animation delay.
                        # NOTE: We add animation delay elsewhere.

    # SPECIAL PLANET SETTINGS
    pen.shape("circle")     # Make the pen look like a planet.
    pen.fillcolor(color)    # Color the planet as requested.

    return {"pen": pen, "a": a, "e": e, "name": name}

##############################################################################

# LIST OF PLANETS TO SIMULATE
# TODO: Add to this in #1, #2, #10, and #11.
planets = [
    make_planet(name="Earth", a=1.000*AU, e=0.017, color="green"),
]

##############################################################################

# INITIALIZE ORBITS
turtle.delay(100) # Take your time on initialization.
for planet in planets:

    # UNPACK THE PLANET dict
    pen = planet["pen"]
    a = planet["a"]
    e = planet["e"]
    name = planet["name"]

    # CALCULATE INITIAL COORDINATES
    x, y = ellipse_coordinates(a, e, 0)

    # PREP THE PEN
    pen.goto(x, y)          # Move the pen to the initial coordinates.
    pen.showturtle()        # Make the "planet" circle visible.
    pen.down()              # Start drawing.
    pen.write("    "+name)  # Label the orbit.
        # NOTE: The spaces before `name`
        #   ensure the label does not overlap with the orbit.

turtle.delay(1) # Speed up for the simulation.

##############################################################################

# RUN THE SIMULATION
for day in range(0, int(TIME), int(STEP)):
    for planet in planets:
        x, y = ellipse_coordinates(planet["a"], planet["e"], day)
        planet["pen"].goto(x, y)

##############################################################################

# PAUSE ON THE FINAL ANIMATION
# NOTE: This line should be uncommented if you are running Python locally.
# turtle.exitonclick()