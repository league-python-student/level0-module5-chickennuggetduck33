"""
Go to the recipe to run the demonstration before starting this program
"""

def setup():
    # Set the size of your sketch to be a rectangle like in the recipe demonstration
    size(600, 400)
    # Call the noFill() command so all the ellipses will be transparent
    noFill()
    global x
    global speed    
    global banana
    global ummwhatthesigma
    x = 51
    speed = 10
    banana = 549
    ummwhatthesigma = 10

def draw():
    background(255,255,255)
    # Use a for loop to make the first set of rings that will start in the left half
    # of the window.

    global x
    global speed
    y = 10
    for i in range(20):
       ellipse(x, 200, y, y)
       y = y + 10
    if x >= 550:
        speed = speed * -1
        
    if x<=50:
        speed = speed * -1
    x = x + speed
    y = 10
    global banana
    global ummwhatthesigma
    for i in range(20):
       ellipse(banana, 200, y, y)
       y = y + 10
    if banana >= 550:
        ummwhatthesigma = ummwhatthesigma * -1
        
    if banana<=50:
        ummwhatthesigma = ummwhatthesigma * -1
    banana = banana + ummwhatthesigma
    # Make this set of rings move across the sketch to the right 
    # Hint: Make two variables, one for x and another for the speed. 
    #       Then increase x by the amount in speed.
        
    # When the rings reach the right side of the sketch, reverse the direction so
    # they move.
    # Hint: speed = -speed */

         
    # When the rings reach the left side of the sketch, reverse the direction again
        
    # CHALLENGE - to finish the Amazing Rings
     
    # Add another for loop to draw the second set of rings that will start in the
    # right half of the window
        
    # Make this set of rings move in the opposite direction to the other rings
    # These rings must also "bounce" off the sides of the window.
