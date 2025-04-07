"""
This is a simple demo script that will output lines that contain a
description, expected sort class, and either True/False indicating
if calling the sort() function output the expected values.

Uses package.sort() to sort the packages rather than the sort() method
on the Package class.
"""

from shipping.package import sort, Stacks

# List of tuples of the form ([width, height, length, weight], expected_output, description)
packages = [
    (
        [30, 20, 10, 5.0],
        Stacks.STANDARD.value,
        "Standard package",
    ),
    (
        [10, 10, 10, 21],
        Stacks.SPECIAL.value,
        "Overweight package",
    ),
    (
        [150, 150, 150, 10],
        Stacks.SPECIAL.value,
        "Oversized package",
    ),
    (
        [150, 150, 150, 21],
        Stacks.REJECTED.value,
        "Rejected package",
    ),
    (
        [150, 150, 150, 21],
        "NOT_A_VALID_STACK",
        "Expected failure package",
    ),
]


for dimensions, expected_output, desc in packages:
    result = sort(*dimensions)
    print(
        f"Testing package: {desc}({expected_output}):\t{result == expected_output}"
    )

    # Uncomment if you want to run the assertion instead of just printing the result
    # assert result == expected_output
