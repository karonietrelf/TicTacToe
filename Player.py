class Player:
    """Class to represent a Player.

        Attributes:
            name (str): A name of the Player.
            sign (str): A sign of the Player. It can be 'O' or 'X'.

        Methods:
        set_sign: Used to set sign to Player. #ustawic
        get_sign: Used to get sign value. #pobrac.
        """

    def __init__(self, player_name):
        self.name = player_name
        self.sign = None

    def set_sign(self, player_sign):
        self.sign = player_sign

    def get_sign(self):
        return self.sign


