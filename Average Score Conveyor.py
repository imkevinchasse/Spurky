# Base Value
average_score = 75

# Scoring differential metrics
poor = range(-101, -5)
below_average = range(-5, 0)
good = range(0, 5)
above_average = range(6, 7)
excellent = range(10, 14)
gifted = range(15, 100)

# Default boolean values.
is_above_average = False
is_below_average = False
is_poor = False
is_good = False
is_excellent = False
is_gifted = False

while True:
    try:
        # Converts score input from string to integer,
        # Then subtracts the average score from the Net score
        score_str = input("What is your score? ")
        Net_score = int(score_str)
        asdifferential = Net_score - average_score

        # Uses the simplified differential to assign boolean values
        if asdifferential in gifted:
            is_gifted = True
        elif asdifferential in excellent:
            is_excellent = True
        elif asdifferential in above_average:
            is_above_average = True
        elif asdifferential in good:
            is_good = True
        elif asdifferential in below_average:
            is_below_average = True
        elif asdifferential in poor:
            is_poor = True

        # Finds which var is true and prints it
        if is_above_average is True:
            print("You scored", asdifferential, "above average.")
        elif is_below_average is True:
            print("You scored", asdifferential, "below average. Study more.")
        elif is_poor is True:
            print("You scored", asdifferential, "poorly. Study more.")
        elif is_good is True:
            print("Your score is average; you can do better.")
        elif is_excellent is True:
            print("Your score is", asdifferential, "above average. Good job!")
        elif is_gifted is True:
            print("You scored", asdifferential, "above average. Amazing!")

        # Exit the loop if the input and processing are successful
        break
    except ValueError:
        print("Invalid input. Please enter a valid number for your score.")
