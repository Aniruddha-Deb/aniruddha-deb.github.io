import random

# Constants
NUM_STUDENTS = 10000
WEEKS_OF_SIMULATION = 6 * 52  # 6 years of simulation in weeks

# Initialize statistics
successful_students = 0

def simulate_school():


# Simulation function for a single student
def simulate_student():
    skill = random.gauss(50, 5)
    grades = random.gauss(50, 5)

    smoking_ctr = 0
    drinking_ctr = 0
    relationship_ctr = 0

    for week in range(1, WEEKS_OF_SIMULATION + 1):
        # Daily study increases skill and grades
        skill_gain = random.randint(1, 5)
        if random.random() < 0.02:
            # Larger variance factor if in a relationship or indulged in drinking/smoking/drugs
            skill_gain = random.gauss(skill_gain, 2)

        skill += skill_gain
        grades += random.randint(1, 5)

        # College decision after 2 years (104 weeks)
        if week == 2 * 52:
            if grades >= 80:
                skill += random.randint(5, 10)
                grades += random.randint(5, 10)

        # Internship interviews after 4 years (208 weeks)
        if week == 4 * 52:
            if skill >= 90:
                skill += random.randint(5, 10)

        # Internship PPO after 5 years (260 weeks)
        if week == 5 * 52:
            if skill >= 95:
                skill += random.randint(5, 10)

        # Placements after 5.5 years (286 weeks)
        if week == 5.5 * 52:
            if skill >= 95:
                successful_students += 1

        # Random decisions every week (e.g., drinking or smoking)
        if random.random() < 0.01:
            # Larger variance factor if in a relationship or indulged in drinking/smoking/drugs
            skill -= random.gauss(1, 2)
            grades -= random.randint(1, 5)

        # Harder decisions every month or two (e.g., relationship or drugs)
        if week % 4 == 0 and random.random() < 0.005:
            # Larger variance factor if in a relationship or indulged in drinking/smoking/drugs
            skill -= random.gauss(5, 2)
            grades -= random.randint(5, 10)

    return skill, grades

# Run the simulation for all students
for _ in range(NUM_STUDENTS):
    skill, grades = simulate_student()
    # Check if the student succeeded in all criteria
    if grades >= 80 and skill >= 95:
        successful_students += 1

# Calculate success rate
success_rate = successful_students / NUM_STUDENTS * 100

# Print results
print(f"Number of successful students: {successful_students}")
print(f"Success rate: {success_rate:.2f}%")
