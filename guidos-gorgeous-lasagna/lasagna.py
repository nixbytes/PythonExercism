"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


# TODO: define the 'EXPECTED_BAKE_TIME' constant.
EXPECTED_BAKE_TIME = 40


# TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(actual_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return int(EXPECTED_BAKE_TIME - actual_bake_time)


# TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider using 'PREPARATION_TIME' here, if you have it defined.
# Calculate preparation time in minutes
def preparation_time_in_minutes(number_of_layers):
    return number_of_layers * 2


# TODO: define the 'elapsed_time_in_minutes()' function below.
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    prep_time = preparation_time_in_minutes(number_of_layers)
    return prep_time + elapsed_bake_time


# Instructions and notes
def main():
    # Calculate remaining bake time
    remaining_bake = bake_time_remaining(30)
    print(f"Remaining bake time: {remaining_bake} minutes")

    # Calculate preparation time
    prep_time = preparation_time_in_minutes(2)
    print(f"Preparation time: {prep_time} minutes")

    # Calculate total elapsed cooking time
    total_time = elapsed_time_in_minutes(3, 20)
    print(f"Total elapsed cooking time: {total_time} minutes")


if __name__ == "__main__":
    main()
