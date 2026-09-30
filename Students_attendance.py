# ============================================================
# Pseudocode Road Map
# ============================================================
# 1. create a student list ✅ : Define a variable / instantiate a list (a list of dictionaries)
# 2. create function with student name as parameter ✅ :Define a function with parameters
# 3. if student is present, add to present list ✅ : Conditional statement (if) / append to a list
# 4. if student is not present, add to absent list ✅ : elif/else branch / append to a list
# 5. display on notice board and call parents ✅ : Print/output / iterate over a list (a for loop)

# ============================================================
# Note: The 'students' mock dataset was generated using AI assistance
# to maintain realistic data variation for testing purposes.
grade_10_students = [
    {"first_name": "Carson", "last_name": "McDaniel"},
    {"first_name": "Hunter", "last_name": "Sutton"},
    {"first_name": "Trevor", "last_name": "McCurdy"},
    {"first_name": "Cadence", "last_name": "Carpenter"},
    {"first_name": "Daniel", "last_name": "Harvin"},
    {"first_name": "Emily", "last_name": "Swisher"},
    {"first_name": "Marissa", "last_name": "Erbach"},
    {"first_name": "Cecelia", "last_name": "Hayes"},
    {"first_name": "Giselle", "last_name": "Brito"},
    {"first_name": "Owen", "last_name": "Wing"},
]

present = []
absent = []


def get_status(first_name, last_name, status):
    """Function to check if student attended class today."""
    full_name = f"{first_name} {last_name}"
    if status == "y":
        present.append(full_name)
    elif status == "n":
        absent.append(full_name)


def take_attendance():
    """Teacher to check if student attended class today."""
    for student in grade_10_students:
        first_name = student["first_name"]
        last_name = student["last_name"]

        print(f"Is {first_name} {last_name} in class today?")
        print("Please key in 'y' for yes or 'n' for no, any other key to exit")
        status = input().strip().lower()

        if status in ("y", "n"):
            get_status(first_name, last_name, status)
        else:
            print("Exiting attendance check early.")
            break


# Run the attendance check
take_attendance()

# Display on the notice board
print("\n----- NOTICE BOARD -----")
print("The following students were present in class today:")
for name in present:
    print(f"  ✓ {name}")

print("\nThe following students were absent from class today:")
for name in absent:
    print(f"  ✗ {name}")

# Call parents of absent students
print("\n----- PARENT NOTIFICATIONS -----")
for name in absent:
    print(f"  📞 Calling parents of {name}...")