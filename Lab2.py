def display_main_menu(temperatures):


    selection = int(input("Please select: "))
    if selection == 5:
        print("Goodbye")
    elif not temperatures and selection != 0:
        print("Please input temperatures first")
    else:
        if selection == 0:
            temperatures = get_user_input()
        elif selection == 1:
            calc_average(temperatures)
        elif selection == 2:
            find_min_max(temperatures)
        elif selection == 3:
            sort_temp(temperatures)
        elif selection == 4:
            calc_median(temperatures)

        display_main_menu(temperatures)


def get_user_input():
    print("Input Temperatures")
    temperatures_input = input("Please enter temperatures, separated by commas: ")
    temperatures = [float(temp) for temp in temperatures_input.split(",")]
    print(temperatures)
    return temperatures


def calc_average(temperatures):
    print("Calculate Average")
    total = sum(temperatures)
    avg = total / len(temperatures)
    print("Average = " + str(avg))
    return avg


def find_min_max(temperatures):
    print("Find Min/Max")
    min_temp = min(temperatures)
    max_temp = max(temperatures)
    print("Minimum temperature: " + str(min_temp))
    print("Maximum temperature: " + str(max_temp))
    return [min_temp, max_temp]


def sort_temp(temperatures):
    print("Sort Temperatures")
    sorted_temperatures = sorted(temperatures)
    print(sorted_temperatures)


def calc_median(temperatures):
    print("Calculate Median")
    temperatures.sort()
    n = len(temperatures)
    if n % 2 == 0:
        median = (temperatures[n // 2 - 1] + temperatures[n // 2]) / 2
    else:
        median = temperatures[n // 2]
    print("Median of the list is: " + str(median))
    return median


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    temperature = []
    display_main_menu(temperature)


if __name__ == "__main__":
    main()
