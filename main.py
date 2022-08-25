#import modules
import math
import pygame as pg
import sys

#define main function
def main():
    running = True
    
    #initialize some variables needed later and create pygame surface
    pi = math.pi

    black = (0, 0, 0)
    white = (255, 255, 255)

    dt = 0.01

    l1 = 100
    l2 = 100

    m1 = 100
    m2 = 100
    thetha1 = pi/4
    thetha2 = pi/8
    
    v1 = 0
    v2 = 0
    g = 9.8
    
    s = pg.display.set_mode([500, 500])
    
    while running:
        x1 = l1 * math.sin(thetha1) + 250
        y1 = l1 * math.cos(thetha1) + 250
        
        x2 = l2 * math.sin(thetha2) + x1
        y2 = l2 * math.cos(thetha2) + y1
        
        s.fill(white)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
        #draw everything        
        pg.draw.line(
            start_pos=(30, 250), end_pos=(470, 250), color=black, surface=s
        )
        pg.draw.line(
            start_pos=(250, 250), end_pos=(x1, y1), color=black, surface=s
        )
        pg.draw.circle(
            center=(x1, y1), radius=(m1 * 0.1), color=black, surface=s
        )
        pg.draw.line(
            start_pos=(x1, y1), end_pos=(x2, y2), color=black, surface=s
        )
        pg.draw.circle(
            center=(x2, y2), radius=(m2 * 0.1), color=black, surface=s
        )
        
        #angular accceleration of rod 1 (physics)
        a1 = ((-g * (2 * m1 + m2) * math.sin(thetha1)) - (m2 * g * math.sin(thetha1-(2*thetha2))) - (2 * math.sin(thetha1-thetha2) * m2 * ((v2 ** 2 * l2) + (v1 * l1 * math.cos(thetha1-thetha2))))) / (l1 * (2 * l1 + m2 - (m2 * math.cos(2 * thetha1 - 2 * thetha2))))
        v1 = v1 + (a1 * dt)
        thetha1 = thetha1 + (v1 * dt)
        
        #angular acceleration of rod 2 (physics)
        a2 = ((2 * math.sin(thetha1-thetha2)) * (((v1**2 * l1 * (m1 + m2))) + ((g * (m1 + m2) * math.cos(thetha1))) + ((v2 ** 2 * l2 * m2 * math.cos(thetha1 - thetha2))))) / (l2 * (2 * m1 + m2 -(m2 * math.cos(2 * thetha1 - 2 * thetha2))))
        v2 = v2 + (a2 * dt)
        thetha2 = thetha2 + (v2 * dt)
        
        #sleep and update screen for smooth fps
        pg.time.wait(1)
        pg.display.update()      

#execute main function        
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()