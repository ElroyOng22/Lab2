def calc_average_temperature(temperatures):
    if not temperatures:
        return 0.0  # Return 0.0 for an empty list
    return sum(temperatures) / len(temperatures)


def calc_min_max_temperature(temperatures):
    if not temperatures:
        return [0, 0]  # Return [0, 0] for an empty list
    return [min(temperatures), max(temperatures)]


if __name__ == "__main__":
    print("Temperature Statistics Calculator")

    # Input temperature data
    temperature_data = [25.5, 30.2, 28.0]

    average_temp = calc_average_temperature(temperature_data)
    min_max_temp = calc_min_max_temperature(temperature_data)

    print(f"Average Temperature: {average_temp:.2f}")
    print(f"Minimum Temperature: {min_max_temp[0]:.2f}")
    print(f"Maximum Temperature: {min_max_temp[1]:.2f}")
