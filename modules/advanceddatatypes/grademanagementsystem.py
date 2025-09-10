'''
Grade Management System
Demonstrates advanced data types: lists, sets, tuples, dictionaries, and string methods
'''

def runsystem():
    '''Run the grade management system'''
 
    print("=== Student Grade Management System ===\n")

    # Dictionary to store all student data
    # Key: student ID, Value: dictionary with student info
    students = {}

    # Set to track unique subjects offered
    subjects = set()

    # List to store grade calculation history
    grade_history = []

    # Tuple for grade boundaries (immutable reference data)
    grade_boundaries = (
        ('A', 90), ('B', 80), ('C', 70), ('D', 60), ('F', 0)
    )

    print("1. Adding students and their grades...\n")

    # Add students with their grade data
    add_student(students, subjects, "ST001", "Alice Johnson", {
        "Math": [95, 87, 92, 89],
        "Science": [88, 91, 85, 93],
        "English": [92, 89, 94, 88]
    })

    add_student(students, subjects, "ST002", "Bob Smith", {
        "Math": [78, 82, 75, 80],
        "Science": [85, 79, 88, 82],
        "History": [90, 87, 89, 91]
    })

    add_student(students, subjects, "ST003", "Carol Davis", {
        "Math": [92, 88, 90, 87],
        "English": [85, 89, 87, 91],
        "Art": [95, 92, 89, 94]
    })

    print("2. System Statistics:")
    print(f"   Total students: {len(students)}")
    print(f"   Subjects offered: {sorted(subjects)}")  # Convert set to sorted list for display
    print(f"   Total unique subjects: {len(subjects)}\n")

    print("3. Processing grades for all students...\n")

    # Process each student's grades
    for student_id, student_data in students.items():
        print(f"--- {student_data['name']} ({student_id}) ---")

        subject_averages = []  # List to store this student's subject averages

        # Calculate average for each subject using string methods for formatting
        for subject, grades in student_data['grades'].items():
            average = sum(grades) / len(grades)
            letter_grade = calculate_letter_grade(average, grade_boundaries)
            subject_averages.append(average)

            # Store in history (demonstrates list operations)
            grade_entry = f"{student_data['name']}-{subject}: {average:.1f} ({letter_grade})"
            grade_history.append(grade_entry)

            print(f"   {subject}: {grades} → Average: {average:.1f} ({letter_grade})")

        # Calculate overall GPA
        overall_average = sum(subject_averages) / len(subject_averages)
        overall_grade = calculate_letter_grade(overall_average, grade_boundaries)
        students[student_id]['gpa'] = overall_average
        students[student_id]['letter_grade'] = overall_grade

        print(f"   Overall GPA: {overall_average:.1f} ({overall_grade})")
        print()

    print("4. Subject Analysis:")
    analyze_subjects_performance(students, subjects)

    print("\n5. Top Performers:")
    find_top_performers(students)

    print("\n6. Grade Distribution:")
    show_grade_distribution(students, grade_boundaries)

    print("\n7. Recent Grade History (last 5 entries):")
    for entry in grade_history[-5:]:  # List slicing to get last 5
        print(f"   {entry}")

    print(f"\nTotal grade calculations performed: {len(grade_history)}")

def add_student(students, subjects, student_id, name, grades):
    """Add a student to the system and update subjects set"""
    students[student_id] = {
        'name': name,
        'grades': grades
    }

    # Add all subjects to the set (automatically handles duplicates)
    for subject in grades.keys():
        subjects.add(subject)

    print(f"Added student: {name} with {len(grades)} subjects")

def calculate_letter_grade(average, grade_boundaries):
    """Calculate letter grade using tuple of boundaries"""
    for letter, min_score in grade_boundaries:
        if average >= min_score:
            return letter
    return 'F'

def analyze_subjects_performance(students, subjects):
    """Analyze performance across all subjects"""
    subject_stats = {}  # Dictionary to store statistics for each subject

    # Initialize dictionary for each subject
    for subject in subjects:
        subject_stats[subject] = []

    # Collect all averages for each subject
    for student_data in students.values():
        for subject, grades in student_data['grades'].items():
            average = sum(grades) / len(grades)
            subject_stats[subject].append(average)

    # Calculate and display statistics
    for subject in sorted(subjects):  # Sort subjects alphabetically
        averages = subject_stats[subject]
        if averages:  # Check if list is not empty
            class_average = sum(averages) / len(averages)
            highest = max(averages)
            lowest = min(averages)
            print(f"   {subject}: Class avg: {class_average:.1f}, "
                  f"Highest: {highest:.1f}, Lowest: {lowest:.1f}")

def find_top_performers(students):
    """Find students with highest GPAs using dictionary operations"""
    # Create list of tuples (gpa, name, student_id) for sorting
    gpa_list = []
    for student_id, data in students.items():
        if 'gpa' in data:  # Make sure GPA was calculated
            gpa_list.append((data['gpa'], data['name'], student_id))

    # Sort by GPA (descending) - tuple comparison sorts by first element
    gpa_list.sort(reverse=True)

    # Display top 3 performers
    print("   Top 3 Students:")
    for i, (gpa, name, student_id) in enumerate(gpa_list[:3]):  # List slicing
        rank = i + 1
        letter = students[student_id]['letter_grade']
        print(f"   {rank}. {name}: {gpa:.1f} ({letter})")

def show_grade_distribution(students, grade_boundaries):
    """Show distribution of letter grades using dictionary counting"""
    grade_counts = {}  # Dictionary to count each letter grade

    # Initialize counts for all possible grades
    for letter, _ in grade_boundaries:
        grade_counts[letter] = 0

    # Count actual grades
    for student_data in students.values():
        if 'letter_grade' in student_data:
            letter = student_data['letter_grade']
            grade_counts[letter] += 1

    # Display distribution
    total_students = len(students)
    for letter, _ in grade_boundaries:
        count = grade_counts[letter]
        percentage = (count / total_students) * 100 if total_students > 0 else 0
        print(f"   {letter}: {count} students ({percentage:.1f}%)")

# Demonstrate string methods with sample student search
def search_students_by_name(students, search_term):
    """Search for students by name using string methods"""
    print(f"\nSearching for students with '{search_term}' in name:")
    found_students = []

    for student_id, data in students.items():
        name = data['name']
        # Use string methods for case-insensitive search
        if search_term.lower() in name.lower():
            found_students.append((student_id, name))

    if found_students:
        for student_id, name in found_students:
            print(f"   Found: {name} ({student_id})")
    else:
        print(f"   No students found with '{search_term}' in their name")

    return found_students

if __name__ == "__main__":
    runsystem()

    # Bonus: Demonstrate additional string operations
    print("\n" + "="*50)
    print("BONUS: Advanced String Operations")
    print("="*50)

    # Sample grade report formatting
    report_template = "Student: {name} | ID: {id} | GPA: {gpa:.2f} | Grade: {grade}"

    sample_data = {
        'name': 'Alice Johnson',
        'id': 'ST001',
        'gpa': 91.5,
        'grade': 'A'
    }

    formatted_report = report_template.format(**sample_data)
    print("\nFormatted Report:")
    print(formatted_report)

    # String manipulation for clean data entry
    messy_input = "  ALICE   johnson  "
    clean_name = messy_input.strip().title()  # Remove whitespace and proper case
    print("\nData cleaning:")
    print(f"Input: '{messy_input}'")
    print(f"Clean: '{clean_name}'")

    # Split/join for handling CSV-like data
    csv_line = "Alice,Johnson,ST001,91.5,A"
    student_fields = csv_line.split(',')
    print("\nCSV parsing:")
    print(f"Raw: {csv_line}")
    print(f"Fields: {student_fields}")

    # Reconstruct with different delimiter
    pipe_format = ' | '.join(student_fields)
    print(f"Reformatted: {pipe_format}")
