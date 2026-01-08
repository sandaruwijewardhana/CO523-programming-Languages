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
    return reduce(lambda total, score: total + score, scores) / len(scores)

def transform_student(student):
    """
    Input: A student dictionary
    Output: A new dictionary with keys: 'id', 'name' (uppercase), and 'final_score' (calculated average)
    """
    return {
        'id': student['id'],
        'name': student['name'].upper(),
        'final_score': calculate_average(student['scores'])
    }

def is_deans_list(student):
    """
    Input: A student dictionary (after transformation)
    Output: Boolean (True if final_score >= 80)
    """
    return student['final_score'] >= 80.0

def format_output(student):
    """
    Input: A student dictionary
    Output: String "ID: [id] | Name: [NAME] | GPA: [score]"
    """
    return f"ID: {student['id']} | Name: {student['name']} | GPA: {student['final_score']:.2f}"

# --- 3. MAIN PIPELINE (Connect the functions) ---

def main():
    # Step A: Transform raw data to calculate averages (Use map)
    processed_students = list(map(transform_student, students_data))

    # Step B: Filter out students below 80.0 (Use filter)
    top_students = list(filter(is_deans_list, processed_students))

    # Step C: Sort students by score descending (Use sorted)
    sorted_students = sorted(top_students, key=lambda s: s['final_score'], reverse=True)

    # Step D: Format the final output strings (Use map)
    final_report = list(map(format_output, sorted_students))

    # Print results (This is the only side effect allowed)
    print("\n--- DEAN'S LIST REPORT ---")
    print(*final_report, sep="\n")

if __name__ == "__main__":
    main()
