class Missile:
    def __init__(self, screen, x):
        # Store the data.  Initialize:   y to 591   and   has_exploded to False.
        # Note: the 591 comes from the screen height (650) minus the ship image height (59).  Best practice would be to
        #   pass in that value in case the ship image or screen height changes, but simplified here to always be 591.
        pass

    def move(self):
        # Make self.y 5 smaller than it was (which will cause the Missile to move UP).
        # Note: you could've instead passed in a speed when you made a Missle, but all missles in the game are the same
        #   speed, so just using a hardcoded 5 is fine.
        pass

    def draw(self):
        # Draw a vertical red (or green) line on the screen for the missile, 8 pixels long,  4 pixels thick
        #   where the line starts at the current position of this Missile.
        pass
