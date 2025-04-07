from enum import Enum


class Stacks(Enum):
    # Enum that represents the different package dispatch stacks
    STANDARD = "STANDARD"
    SPECIAL = "SPECIAL"
    REJECTED = "REJECTED"


class Package:
    """
    Class that represents a package being shipped.

    Class Constants:
        MAX_WEIGHT (float): Maximum weight of a package in kilograms
        MAX_VOLUME (float): Maximum volume of a package in cubic centimeters
        MAX_DIMENSION (float): Maximum dimension of a package in centimeters
    """

    MAX_WEIGHT = 20  # In kg
    MAX_VOLUME = 1000000  # In cm³
    MAX_DIMENSION = 150  # In cm

    def __init__(
        self, width: float, height: float, length: float, weight: float
    ):
        """
        Initialize a Package instance.

        Args:
            width (float): Width of the package in centimeters
            height (float): Height of the package in centimeters
            length (float): Length of the package in centimeters
            weight (float): Weight of the package in kilograms
        """
        self.width = width
        self.height = height
        self.length = length
        self.weight = weight

    def is_heavy(self) -> bool:
        """
        Return True if the package weighs greater than or equal to 
        Package.MAX_WEIGHT
        """
        return self.weight >= self.MAX_WEIGHT

    def is_bulky(self) -> bool:
        """
        Return True if the package is bulky which is defined as having a
        volume greater than or equal to Package.MAX_VOLUME or any dimension
        greater than or equal to Package.MAX_DIMENSION
        """
        return self.get_volume() >= self.MAX_VOLUME or self.is_oversized()

    def get_volume(self) -> float:
        return self.width * self.height * self.length

    def is_oversized(self) -> bool:
        """
        Check if any dimension exceeds the maximum allowed dimension.

        Returns:
            bool: True if any dimension exceeds max_dimension, 
                    False otherwise
        """
        return any(
            dim >= self.MAX_DIMENSION
            for dim in [self.width, self.height, self.length]
        )

    def sort(self) -> str:
        """
        Sort a package into one of three categories based on size and 
        weight and return the category as a string
        """
        if self.is_bulky() and self.is_heavy():
            return Stacks.REJECTED.value
        elif self.is_bulky() or self.is_heavy():
            return Stacks.SPECIAL.value
        else:
            return Stacks.STANDARD.value


def sort(width, height, length, mass):
    """
    Sort a package into one of three categories based on the dimensions and
    weight of the package.

    Args:
        width (float): Width of the package in centimeters
        height (float): Height of the package in centimeters
        length (float): Length of the package in centimeters
        mass (float): Weight of the package in kilograms
    """
    package = Package(width, height, length, mass)
    return package.sort()
