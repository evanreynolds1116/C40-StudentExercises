from exercise import Exercise
from cohort import Cohort
from instructor import Instructor
from student import Student

# Once you have defined all of your custom types, go to main.py, import the classes you need, and implement the following logic.

# Create 4, or more, exercises.
# Create 3, or more, cohorts.
# Create 4, or more, students and assign them to one of the cohorts.
# Create 3, or more, instructors and assign them to one of the cohorts.
# Have each instructor assign 2 exercises to each of the students.

create_list = Exercise("Create list", "Python")
create_dictionary = Exercise("Create dictionary", "Python")
create_tuple = Exercise("Create tuple", "Python")
create_set = Exercise("Create set", "Python")
comprehensions = Exercise("Comprehensions", "Python")
functions = Exercise("Functions", "Python")

cohort_40 = Cohort("Cohort 40")
cohort_41 = Cohort("Cohort 41")
cohort_42 = Cohort("Cohort 42")

evan_reynolds = Student("Evan", "Reynolds", "Evan-Reynolds", cohort_40)
roxanne_nasraty = Student("Roxanne", "Nasraty", "Roxanne-Nasraty", cohort_40)
john_smith = Student("John", "Smith", "John-Smith", cohort_41)
jane_doe = Student("Jane", "Doe", "Jane-Doe", cohort_42)

joe_shepherd = Instructor("Joe", "Shepherd", "Joe-Shepherd", cohort_40, "jokes")
bryan_nilsen = Instructor("Bryan", "Nilsen", "Bryan-Nilsen", cohort_41, "high-fives")
maddi_peper = Instructor("Madi", "Peper", "Madi-Peper", cohort_42, "smiles")

joe_shepherd.assign_exercise(create_list, evan_reynolds)
joe_shepherd.assign_exercise(create_list, roxanne_nasraty)
joe_shepherd.assign_exercise(create_list, john_smith)
joe_shepherd.assign_exercise(create_list, jane_doe)
joe_shepherd.assign_exercise(create_dictionary, evan_reynolds)
joe_shepherd.assign_exercise(create_dictionary, roxanne_nasraty)
joe_shepherd.assign_exercise(create_dictionary, john_smith)
joe_shepherd.assign_exercise(create_dictionary, jane_doe)

bryan_nilsen.assign_exercise(create_tuple, evan_reynolds)
bryan_nilsen.assign_exercise(create_tuple, roxanne_nasraty)
bryan_nilsen.assign_exercise(create_tuple, john_smith)
bryan_nilsen.assign_exercise(create_tuple, jane_doe)
bryan_nilsen.assign_exercise(create_set, evan_reynolds)
bryan_nilsen.assign_exercise(create_set, roxanne_nasraty)
bryan_nilsen.assign_exercise(create_set, john_smith)
bryan_nilsen.assign_exercise(create_set, jane_doe)

maddi_peper.assign_exercise(comprehensions, evan_reynolds)
maddi_peper.assign_exercise(comprehensions, roxanne_nasraty)
maddi_peper.assign_exercise(comprehensions, john_smith)
maddi_peper.assign_exercise(comprehensions, jane_doe)
maddi_peper.assign_exercise(comprehensions, evan_reynolds)
maddi_peper.assign_exercise(comprehensions, roxanne_nasraty)
maddi_peper.assign_exercise(comprehensions, john_smith)
maddi_peper.assign_exercise(comprehensions, jane_doe)





