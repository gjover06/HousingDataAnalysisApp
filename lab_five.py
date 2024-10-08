"""
name: George Samu
subject: SDEV 300
"""
import pandas as pd
import matplotlib.pyplot as plt

# def get_menu():
#    """Getting menu"""
menu = """
    ***************** Welcome to the Python Housing Data Analysis App**********
    Select the file you want to analyze:
    1. Population Data
    2. Housing Data
    3. Exit the Program
    """


def get_Pop_Apr_1_histogram():
    """showing histogram """
    # plt.hist(the_population[["Pop Apr 1"]], bins=10)
    the_population[["Pop Apr 1"]].hist()
    plt.xlabel("Pop Apr 1")
    plt.ylabel("count")
    plt.title("The population of April 1")
    plt.show()


def get_Pop_Jul_1_histogram():
    """ showing histogram"""
    the_population[["Pop Jul 1"]].hist()
    plt.xlabel("Pop Jul 1")
    plt.ylabel("count")
    plt.title("The population of Jul 1")
    plt.show()


def get_Change_Pop_histogram():
    """ showing histogram"""
    the_population[["Change Pop"]].hist()
    plt.xlabel("Change Pop")
    plt.ylabel("count")
    plt.title("The population change")
    plt.show()


def get_Age_histogram():
    """ showing histogram"""
    the_housing[["AGE"]].hist()
    plt.xlabel("Age")
    plt.ylabel("count")
    plt.title("The Age")
    plt.show()


def get_Bedroom_histogram():
    """ showing histogram"""
    the_housing[["BEDRMS"]].hist()
    plt.xlabel("BEDRoomS")
    plt.ylabel("count")
    plt.title("The number of bed rooms")
    plt.show()


def get_Built_histogram():
    """showing histogram """
    the_housing[["BUILT"]].hist()
    plt.xlabel("years built")
    plt.ylabel("count")
    plt.title("The houses built by year")
    plt.show()


def get_Rooms_histogram():
    """showing histogram """
    the_housing[["ROOMS"]].hist()
    plt.xlabel("number of rooms")
    plt.ylabel("count")
    plt.title("The number of rooms")
    plt.show()


def get_Utility_histogram():
    """ showing histogram"""
    the_housing[["UTILITY"]].hist()
    plt.xlabel("Utility prices")
    plt.ylabel("count")
    plt.title("The prices of utility")
    plt.show()


# print(get_menu())
def pop_data():
    """ Running function on pop data"""
    sub_menu = """
        You have entered Population Data.
        Select the Column you want to analyze:
        a. Pop Apr 1
        b. Pop Jul 1
        c. Change Pop
        d. Exit Column
    """
    while True:
        print(sub_menu)
        menu_number = input("")
        if menu_number.lower() == 'a':
            print("You've chosen a")
            count = the_population[["Pop Apr 1"]].count()
            mean = the_population[["Pop Apr 1"]].mean()
            minimum = the_population[["Pop Apr 1"]].min()
            maximum = the_population[["Pop Apr 1"]].max()
            standard_deviation = the_population[["Pop Apr 1"]].std()
            # get histogram
            print(f"count: {count}")
            print(f"mean: {mean}")
            print(f"minimum: {minimum}")
            print(f"maximum: {maximum}")
            print(f"Standard deviation: {standard_deviation}")
            # APr 1 histogram
            print("The Histogram of this column is now displayed. ")
            print(get_Pop_Apr_1_histogram())
        elif menu_number.lower() == 'b':
            print("you've chosen b")
            # Variables for Pop Jul 1
            count = the_population[["Pop Jul 1"]].count()
            mean = the_population[["Pop Jul 1"]].mean()
            minimum = the_population[["Pop Jul 1"]].min()
            maximum = the_population[["Pop Jul 1"]].max()
            standard_deviation = the_population[["Pop Jul 1"]].std()
            # print minimum, count, mean, maximum
            print(f"count: {count}")
            print(f" mean: {mean}")
            print(f"minimum: {minimum}")
            print(f" maximum: {maximum}")
            print(f"standard deviation: {standard_deviation}")
            # print histogram
            print("The Histogram of this column is now displayed. ")
            print(get_Pop_Jul_1_histogram())
        elif menu_number.lower() == 'c':
            print("you've chosen c")
            # variables for change pop
            count = the_population[["Change Pop"]].count()
            mean = the_population[["Change Pop"]].mean()
            minimum = the_population[["Change Pop"]].min()
            maximum = the_population[["Change Pop"]].max()
            standard_deviation = the_population[["Change Pop"]].std()
            # print change Pop count mean min max and STD
            print(f"count: {count}")
            print(f" mean: {mean}")
            print(f"minimum: {minimum}")
            print(f" maximum: {maximum}")
            print(f"standard deviation: {standard_deviation}")
            # print histogram
            print("The Histogram of this column is now displayed. ")
            print(get_Change_Pop_histogram())
        elif menu_number.lower() == 'd':
            # using break to exit column
            break
        else:
            print("You have chosen the wrong option please choose again")
            print(sub_menu)
            menu_number = input("")


def housing_data():
    """running function on housing data"""
    sub_menu = """
           You have entered Housing Data.
           Select the Column you want to analyze:
           a. Age
           b. Bedrooms
           c. Built
           d. Rooms
           e. Utility
           f. Exit Column
    """
    while True:
        print(sub_menu)
        housing_menu = input(" ")
        if housing_menu.lower() == "a":
            print(" The age")
            # variables for age
            count = the_housing[["AGE"]].count()
            mean = the_housing[["AGE"]].mean()
            minimum = the_housing[["AGE"]].min()
            maximum = the_housing[["AGE"]].max()
            standard_deviation = the_housing[["AGE"]].std()
            # print age
            print(f"count: {count}")
            print(f" mean: {mean}")
            print(f"minimum: {minimum}")
            print(f" maximum: {maximum}")
            print(f"standard deviation: {standard_deviation}")
            # print histogram
            print("The Histogram of this column is now displayed. ")
            print(get_Age_histogram())
        elif housing_menu.lower() == "b":
            print("The bedrooms")
            # variables for BEDRMS
            count = the_housing[["BEDRMS"]].count()
            mean = the_housing[["BEDRMS"]].mean()
            minimum = the_housing[["BEDRMS"]].min()
            maximum = the_housing[["BEDRMS"]].max()
            standard_deviation = the_housing[["BEDRMS"]].std()
            # print count mean min max and std for BEDRMS
            print(f"count: {count}")
            print(f" mean: {mean}")
            print(f"minimum: {minimum}")
            print(f" maximum: {maximum}")
            print(f"standard deviation: {standard_deviation}")
            # print bedroom histogram
            print("The Histogram of this column is now displayed. ")
            print(get_Bedroom_histogram())
        elif housing_menu.lower() == "c":
            print("BUILT")
            # variables for BUILT
            count = the_housing[["BUILT"]].count()
            mean = the_housing[["BUILT"]].mean()
            minimum = the_housing[["BUILT"]].min()
            maximum = the_housing[["BUILT"]].max()
            standard_deviation = the_housing[["BUILT"]].std()
            # print count mean min max and std for BUILT
            print(f"count: {count}")
            print(f" mean: {mean}")
            print(f"minimum: {minimum}")
            print(f" maximum: {maximum}")
            print(f"standard deviation: {standard_deviation}")
            # print built histogram
            print("The Histogram of this column is now displayed. ")
            print(get_Built_histogram())
        elif housing_menu.lower() == "d":
            print("ROOMS")
            count = the_housing[["ROOMS"]].count()
            mean = the_housing[["ROOMS"]].mean()
            minimum = the_housing[["ROOMS"]].min()
            maximum = the_housing[["ROOMS"]].max()
            standard_deviation = the_housing[["ROOMS"]].std()
            # print count mean min max and std for ROOMS
            print(f"count: {count}")
            print(f" mean: {mean}")
            print(f"minimum: {minimum}")
            print(f" maximum: {maximum}")
            print(f"standard deviation: {standard_deviation}")
            # print histogram
            print("The Histogram of this column is now displayed. ")
            print(get_Rooms_histogram())
        elif housing_menu.lower() == "e":
            print("UTILITY")
            count = the_housing[["UTILITY"]].count()
            mean = the_housing[["UTILITY"]].mean()
            minimum = the_housing[["UTILITY"]].min()
            maximum = the_housing[["UTILITY"]].max()
            standard_deviation = the_housing[["UTILITY"]].std()
            # print count mean min max and std for UTILITY
            print(f"count: {count}")
            print(f" mean: {mean}")
            print(f"minimum: {minimum}")
            print(f" maximum: {maximum}")
            print(f"standard deviation: {standard_deviation}")
            # print historgram
            print("The Histogram of this column is now displayed. ")
            print(get_Utility_histogram())
        elif housing_menu.lower() == "f":
            # exit column
            print("exited column")
            break
        else:
            print("Please select an option within the parameters")
            print(sub_menu)
            housing_menu = input(" ")


# the_population = pd.read_csv('PopChange.csv', names= ['Pop Apr 1', 'Pop Jul 1', 'Change Pop' ])
the_population = pd.read_csv('PopChange.csv', usecols=[4, 5, 6])

the_housing = pd.read_csv('Housing.csv', usecols=[0, 1, 2, 4, 6])
while True:
    print(menu)
    try:
        menu_number = int(input(""))
    except ValueError:
        print("Please enter a integer between 1-3")
    else:
        if menu_number == 1:
            # print("population data")
            pop_data()
        # print(the_population)
        elif menu_number == 2:
            print("Housing data")
            housing_data()
        elif menu_number == 3:
            print("exit the program")

        else:
            print("This is not a menu option")
