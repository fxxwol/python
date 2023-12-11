from abc import ABC, abstractmethod
import colorama
from colorama import Fore
import os

colorama.init(autoreset=True)

colors = dict(enumerate(sorted(Fore.__dict__.keys())))

class Figure3D(ABC):
    """
    An abstract base class representing a 3D figure.

    Attributes:
    - `_character` (str): The character representing the shape.
    - `_color_position` (int): The position of the color in the available colors.

    Methods:
    - `get_2d_representation() -> list`: Abstract method to get the 2D representation of the figure.
    - `get_3d_representation(scale: float = 1.0) -> str`: Abstract method to get the 3D representation of the figure.
    - `is_appropriate_character(character: str) -> bool`: Static method to check if the character is appropriate.

    Usage example:
    ```python
    class MyFigure(Figure3D):
        # Implement abstract methods here...
    ```
    """

    def __init__(self, character: str, color_position: int):
        """
        Initialize a Figure3D object with a character and color position.

        Parameters:
        - `character` (str): The character representing the shape.
        - `color_position` (int): The position of the color in the available colors.

        Raises:
        - `ValueError`: If the color position is not in the range of available colors.
        - `ValueError`: If the character is not appropriate (not a single character).
        """
        if not colors.__contains__(color_position):
            raise ValueError("Color position must be in the range of available colors")
        elif not Figure3D.is_appropriate_character(character):
            raise ValueError(
                "Only one character is allowed as the figure's representation"
            )
        self._character = character
        self._color_position = color_position

    @abstractmethod
    def get_2d_representation(self) -> list:
        """
        Abstract method to get the 2D representation of the figure.

        Returns:
        list: A list of strings representing the 2D representation.

        Usage example:
        ```python
        class MyFigure(Figure3D):
            def get_2d_representation(self) -> list:
                # Implement the 2D representation...
        ```
        """
        pass

    @abstractmethod
    def get_3d_representation(self, scale: float = 1.0) -> str:
        """
        Abstract method to get the 3D representation of the figure.

        Parameters:
        - `scale` (float): The scale factor for the 3D representation.

        Returns:
        str: A string representing the 3D representation.

        Usage example:
        ```python
        class MyFigure(Figure3D):
            def get_3d_representation(self, scale: float = 1.0) -> str:
                # Implement the 3D representation...
        ```
        """
        pass

    @staticmethod
    def is_appropriate_character(character: str) -> bool:
        """
        Check if the character is appropriate (a single character).

        Parameters:
        - `character` (str): The character to check.

        Returns:
        bool: True if the character is appropriate, False otherwise.

        Usage example:
        ```python
        if Figure3D.is_appropriate_character("A"):
            # Proceed with the appropriate character...
        ```
        """
        return len(character) == 1

