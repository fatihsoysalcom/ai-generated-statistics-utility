import collections

def calculate_basic_stats(data_list):
    """
    Calculates mean, median, and mode for a list of numbers.
    This function simulates a common utility that an AI code generator
    might produce to help automate data analysis tasks, showcasing its ability
    to quickly generate functional code for repetitive or slightly complex logic.
    """
    if not data_list:
        # AI-generated code often includes basic error handling or edge case checks.
        return {"mean": None, "median": None, "mode": "No data"}

    # Calculate mean (average) - a straightforward calculation AI can easily provide.
    mean_val = sum(data_list) / len(data_list)

    # Calculate median - requires sorting and conditional logic for even/odd length,
    # which AI tools handle well to produce correct implementations.
    sorted_data = sorted(data_list)
    n = len(sorted_data)
    if n % 2 == 0:
        median_val = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        median_val = sorted_data[n // 2]

    # Calculate mode - involves counting frequencies and finding the most frequent.
    # AI can generate this logic using standard library tools like collections.Counter.
    counts = collections.Counter(data_list)
    max_count = 0
    mode_vals = []

    if counts:
        max_count = max(counts.values())
        # If all elements are unique (max_count is 1 and count of unique elements equals total elements),
        # then there's no distinct mode. AI can be prompted to handle such nuances.
        if max_count == 1 and len(counts) == len(data_list):
            mode_vals = [] # Indicate no distinct mode
        else:
            mode_vals = [key for key, value in counts.items() if value == max_count]

    return {
        "mean": mean_val,
        "median": median_val,
        "mode": mode_vals if mode_vals else "No distinct mode"
    }

if __name__ == "__main__":
    print("--- Demonstrating AI-Generated-like Statistical Functions ---")
    print("This script showcases a utility function that an AI code generator")
    print("could quickly produce, automating common data processing tasks.\n")

    sample_data_1 = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
    sample_data_2 = [10, 20, 30, 40, 50] # No distinct mode
    sample_data_3 = [1, 1, 2, 2, 3, 3] # Multiple modes
    sample_data_4 = [] # Edge case: empty list
    sample_data_5 = [7] # Single element list

    test_cases = {
        "Sample Data 1 (Common Case)": sample_data_1,
        "Sample Data 2 (No Distinct Mode)": sample_data_2,
        "Sample Data 3 (Multiple Modes)": sample_data_3,
        "Sample Data 4 (Empty List)": sample_data_4,
        "Sample Data 5 (Single Element)": sample_data_5,
    }

    for name, data in test_cases.items():
        print(f"--- {name} ---")
        stats = calculate_basic_stats(data)
        print(f"Input Data: {data}")
        print(f"Mean: {stats['mean'] if stats['mean'] is not None else 'N/A'}")
        print(f"Median: {stats['median'] if stats['median'] is not None else 'N/A'}")
        print(f"Mode: {stats['mode']}")
        print("\n")

    print("This example highlights how AI assists developers by providing ready-to-use")
    print("code for common patterns, enhancing productivity and reducing boilerplate.")
