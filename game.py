import pygame

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (25, 200, 25)

class Game:
    """A class to help manage gameplay"""

    def __init__(self, player, zombie_group, platform_group, portal_group, bullet_group, ruby_group):
        """Initialize the game"""
        pass


    def update(self):
        """Update the game"""
        pass


    def draw(self):
        """Draw the game HUD"""
        pass


    def add_zombie(self):
        """Add a zombie to the game"""
        pass


    def check_collisions(self):
        """Check collisions that affect gameplay"""
        pass


    def check_round_completion(self):
        """Check if the player survived a single night"""
        pass


    def check_game_over(self):
        """Check to see if the player lost the game"""
        pass


    def start_new_round(self):
        """Start a new night"""
        pass


    def pause_game(self, main_text, sub_text):
        """Pause the game"""
        pass


    def reset_game(self):
        """Reset the game"""
        pass
