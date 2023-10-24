def calc_average_temperature(temperatures):
    if not temperatures:
        return 0.0  # Return 0.0 for an empty list
    return sum(temperatures) / len(temperatures)


def calc_min_max_temperature(temperatures):
    if not temperatures:
        return [0, 0]  # Return [0, 0] for an empty list
    return [min(temperatures), max(temperatures)]


def calc_median_temperature(temperatures):
    if not temperatures:
        return 0.0  # Return 0.0 for an empty list

    # Sort the list of temperatures in ascending order
    temperatures.sort()

    n = len(temperatures)

    # If the number of elements is odd, return the middle element
    if n % 2 == 1:
        return temperatures[n // 2]

    # If the number of elements is even, return the average of the two middle elements
    mid1 = temperatures[(n - 1) // 2]
    mid2 = temperatures[n // 2]
    return (mid1 + mid2) / 2


def main():
    print("Temperature Statistics Calculator")

    temperature_data = [25.5, 30.2, 28.0, 27.7, 26.9]

    average_temp = calc_average_temperature(temperature_data)
    min_max_temp = calc_min_max_temperature(temperature_data)
    median_temp = calc_median_temperature(temperature_data)

    print(f"Average Temperature: {average_temp:.2f}")
    print(f"Minimum Temperature: {min_max_temp[0]:.2f}")
    print(f"Maximum Temperature: {min_max_temp[1]:.2f}")
    print(f"Median Temperature: {median_temp:.2f}")

if __name__ == "__main__":
    main()