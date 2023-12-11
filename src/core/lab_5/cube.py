from colorama import Fore
from src.classes.colors_handling import ColorProcessor
from src.core.lab_5.figure import Figure3D
import colorama
from colorama import Fore

colorama.init(autoreset=True)
colors = dict(enumerate(sorted(Fore.__dict__.keys())))

class Cube(Figure3D):
    """
    A concrete class representing a cube in 3D space.

    Attributes:
    - `__length` (int): The length of the cube's sides.
    - `__offset` (int): The offset for 3D representation.

    Methods:
    - `get_2d_representation() -> list`: Get the 2D representation of the cube.
    - `get_3d_representation(scale: float = 1.0) -> str`: Get the 3D representation of the cube.

    Usage example:
    ```python
    cube = Cube(length=5, character="*", color_position=1)
    cube_2d_representation = cube.get_2d_representation()
    cube_3d_representation = cube.get_3d_representation(scale=2.0)
    ```
    """

    def __init__(self, length: int, character: str, color_position: int):
        """
        Initialize a Cube object with a specified length, character, and color position.

        Parameters:
        - `length` (int): The length of the cube's sides.
        - `character` (str): The character representing the cube.
        - `color_position` (int): The position of the color in the available colors.

        Raises:
        - `ValueError`: If the specified length is not greater than 0.
        """
        if length <= 0:
            raise ValueError("Length must be greater than 0")
        super().__init__(character, color_position)
        self.__length = length
        self.__offset = int(length / 2 + 1)

    def get_2d_representation(self) -> list:
        """
        Get the 2D representation of the cube.

        Returns:
        list: A list of strings representing the 2D representation.

        Usage example:
        ```python
        cube = Cube(length=5, character="*", color_position=1)
        cube_2d_representation = cube.get_2d_representation()
        ```
        """
        result = ""
        for row in range(self.__length):
            for col in range(self.__length):
                if row == 0 or row == self.__length - 1:
                    result += f"{self._character}  "
                elif col == 0 or col == self.__length - 1:
                    result += f"{self._character}  "
                else:
                    result += "   "
            result += "\n"

        return [
            (Fore.__getattribute__(colors[self._color_position]) + "\n" + result)
            for _ in range(6)
        ]

    def get_3d_representation(self, scale: float = 1.0) -> str:
        """
        Get the 3D representation of the cube.

        Parameters:
        - `scale` (float): The scale factor for the 3D representation.

        Returns:
        str: A string representing the 3D representation.

        Usage example:
        ```python
        cube = Cube(length=5, character="*", color_position=1)
        cube_3d_representation = cube.get_3d_representation(scale=2.0)
        ```
        """
        modified_length = (
            int(self.__length * scale) if self.__length * scale >= 2 else self.__length
        )
        modified_offset = int(modified_length / 2 + 1)
        result = ""

        for row in range(modified_offset - 1):
            for col in range(modified_length + modified_offset - 1):
                if (row + col == modified_offset - 1) or (
                    row == 0 and col > modified_offset - 1
                ):
                    result += f"{self._character}" + (
                        ""
                        if col == modified_length + modified_offset - 2 and row == 0
                        else "  "
                    )
                elif modified_length + modified_offset - row == col + 2:
                    result += f"{self._character}"
                elif col == modified_length + modified_offset - 2:
                    result += f"  {self._character}"
                else:
                    result += "   "
            result += "\n"

        for row in range(modified_length):
            for col in range(modified_length + modified_offset):
                if (
                    (row == 0 or row == modified_length - 1)
                    and col < modified_length
                    or (col == 0 or col == modified_length - 1)
                    and row < modified_length
                    and col < modified_length
                ):
                    result += f"{self._character}" + (
                        ""
                        if row == modified_length - 1 and col == modified_length - 1
                        else "  "
                    )
                elif (
                    row + col == (modified_length - 1) * 2
                    and col < modified_length + modified_offset - 1
                ):
                    result += "   " * (modified_length - row - 2) + f"{self._character}"
                elif col < modified_length and row < modified_length:
                    result += "   "
                elif row < modified_length - modified_offset and col > modified_length:
                    if col == modified_offset + modified_length - 1:
                        result += f"{self._character}"
                    else:
                        result += "   "

            result += "\n"

        return Fore.__getattribute__(colors[self._color_position]) + "\n" + result
