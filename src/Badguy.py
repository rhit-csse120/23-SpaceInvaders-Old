class Badguy:
    def __init__(self, screen, x, y, speed):
        # Store the given arguments as instance variables with the same names.
        # Set   is_dead to False   and   original_x to x   and move_right to True.
        # Load the file  "badguy.png"  as the image. and set its colorkey to black.
        pass

    def move(self):
        # Move self.speed units horizontally in the current direction.
        # If this Badguy's horizontal position is more than 100 pixels from its original x position, then...
        #     change the direction
        #     move the y down 4 * self.speed units
        pass

    def draw(self):
        # Draw this Badguy, using its image at its current (x, y) position.
        pass

    def is_hit_by(self, missile):
        # Make a Badguy hitbox rect.
        # Return True if that hitbox collides with the xy point of the given missile.
        pass
