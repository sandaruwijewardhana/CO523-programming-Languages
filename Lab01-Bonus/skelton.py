from functools import reduce

# --- 1. IMMUTABLE DATASET (Do not modify) ---
students_data = [
    {'id': 101, 'name': 'alice', 'scores': [88, 76, 92, 85]},
    {'id': 102, 'name': 'bob', 'scores': [70, 65, 80, 72]},
    {'id': 103, 'name': 'charlie', 'scores': [95, 100, 92, 98]},
    {'id': 104, 'name': 'diana', 'scores': [82, 85, 79, 81]},
    {'id': 105, 'name': 'evan', 'scores': [60, 55, 62, 58]}
]

# --- 2. HELPER FUNCTIONS (Implement these purely) ---

def calculate_average(scores):
    """
    Input: List of integers (e.g., [88, 76, 92, 85])
    Output: Float (Average of the scores)
    CONSTRAINT: Use reduce() here. No loops.
    """
    # TODO: Implement using reduce
    pass

def transform_student(student):
    """
    Input: A student dictionary
    Output: A new dictionary with keys: 'id', 'name' (uppercase), and 'final_score' (calculated average)
    """
    # TODO: Use calculate_average() inside here
    pass

def is_deans_list(student):
    """
    Input: A student dictionary (after transformation)
    Output: Boolean (True if final_score >= 80)
    """
    # TODO: Return True/False
    pass

def format_output(student):
    """
    Input: A student dictionary
    Output: String "ID: [id] | Name: [NAME] | GPA: [score]"
    """
    # TODO: Format the string
    pass

# --- 3. MAIN PIPELINE (Connect the functions) ---

def main():
    # Step A: Transform raw data to calculate averages (Use map)
    processed_students = # TODO

    # Step B: Filter out students below 80.0 (Use filter)
    top_students = # TODO

    # Step C: Sort students by score descending (Use sorted)
    sorted_students = sorted(top_students, key=lambda s: s['final_score'], reverse=True)

    # Step D: Format the final output strings (Use map)
    final_report = # TODO

    # Print results (This is the only side effect allowed)
    print("\n--- DEAN'S LIST REPORT ---")
    print(*final_report, sep="\n")

if __name__ == "__main__":
    main()