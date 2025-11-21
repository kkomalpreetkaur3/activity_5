"""This module defines the Team class."""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"

from  player.player import Player

class Team:
    """Represents a sports team made up of Player objects."""

    def __init__(self, name: str):
        """Initializes a new Team.

        Args:
            name (str): The name of the team.

        Raises:
            ValueError: If name is not a string.
        """

        if not isinstance(name, str):
            raise ValueError("Name must be a string")

        self.__name = name
        self.__players = []

    @property
    def name(self) -> str:
        """Gets the name of the team."""
        return self.__name

    @property
    def players(self) -> list:
        """Gets the list of players in the team."""
        return self.__players

    def add_player(self, player: Player) -> None:
        """Adds a player to the team.

        Args:
            player (Player): Player to add.

        Raises:
            ValueError: If player is not an instance of Player.
        """

        if not isinstance(player, Player):
            raise ValueError("player must be a Player instance")

        self.__players.append(player)

    def __str__(self) -> str:
        """Returns string representation of team."""
        players = ", ".join(str(p) for p in self.__players)
        return f"Team: {self.__name} | Players: [{players}]"

