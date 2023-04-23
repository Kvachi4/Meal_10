"""Is it Meal Time?"""

def main():
    """Main function by - ლაშა კვაჭაძე"""
    meal_time = convert(input("What time is it? "))
    if meal_time >= 7.0 and meal_time <= 8.0:
        print("breakfast time")
    elif meal_time >= 12.0 and meal_time <= 13.0:
        print("lunch time")
    elif meal_time >= 18.0 and meal_time <= 19.0:
        print("dinner time")


def convert(time):
    """Convert function by - ლაშა კვაჭაძე"""
    hours, minutes = time.split(":")
    float_time = hours + "." + minutes
    my_time = float(float_time)
    return my_time


if __name__ == "__main__":
    main()
