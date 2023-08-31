# lasagna.py

# Define expected bake time in minutes
EXPECTED_BAKE_TIME = 40


# Calculate remaining bake time in minutes
def bake_time_remaining(actual_bake_time):
    """Calculate the remaining bake time based on the expected bake time.

    :param actual_bake_time: int - the time the lasagna has been in the oven.
    :return: int - remaining bake time in minutes.

    This function takes the actual time the lasagna has been baking and calculates
    the remaining time needed to reach the expected bake time.
    """
    return EXPECTED_BAKE_TIME - actual_bake_time


# Calculate preparation time in minutes
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time based on the number of layers.

    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - preparation time in minutes.

    This function calculates the preparation time based on the assumption that
    each layer takes 2 minutes to prepare.
    """
    return number_of_layers * 2


# Calculate total elapsed cooking time (prep + bake) in minutes
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
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
