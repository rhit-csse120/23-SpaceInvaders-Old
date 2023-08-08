class Fighter:
    def __init__(self, screen, x, y):
        # Store the screen, x and y to instance variables.
        # Set   self.missiles   to the empty list [ALREADY DONE].
        # Load the file  "fighter.png"  as the image.
        # Set the colorkey to white (it has a white background that needs removed) using the method set_colorkey
        self.missiles = []

    def draw(self):
        # Draw this Fighter, using its image at its current (x, y) position.
        pass

    def fire(self):
        # Construct a new Missile self.image.get_width() / 2 pixels to the right of this Fighter's x position.
        # Append that Missile to this Fighter's list of Missile objects.
        pass

    def remove_exploded_missiles(self):
        # Already complete
        for k in range(len(self.missiles) - 1, -1, -1):
            if self.missiles[k].has_exploded or self.missiles[k].y < -8:
                del self.missiles[k]
