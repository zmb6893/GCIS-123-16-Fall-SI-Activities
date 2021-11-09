"""
Session 12A: Classes and constructors
"""

# Make a person class that holds the state for a name, age, and mood
class Person:
    # Refactor the code so that the person class only accepts use of the variables defined above.
    __slots__ = ['name', 'age', 'mood', 'favoriteHobby', 'courses']

    # Make a constructor for this class
    def __init__(self, name, age, mood):
        self.name = name
        self.age = age
        self.mood = mood
        self.courses = []


# Make a course class that holds the state for course_name, course_number, and number_of_students
# Once you have completed the above step, add a state for courses to the person class
class Course:
    # Refactor the code so that the person class only accepts use of the variables defined above.
    __slots__ = ['course_id', 'professor', 'number_of_students']

    # Make a constructor for this class
    def __init__(self,course_id, professor, number_of_students):
        self.course_id = course_id
        self.professor = professor
        self.number_of_students = number_of_students

# Make a class for a favorite hobby that has fields for hobby_name and description
# Once you've have completed this step, add the state for favorite hobby to the person class
class FavoriteHobby:
    # Refactor the code so that the person class only accepts use of the variables defined above.
    __slots__ = ['hobby_name', 'description']

    # Make a constructor for this class
    def __init__(self, hobby_name, description):
        self.hobby_name = hobby_name
        self.description = description

def main():
    # instantiate a person class with default values
    person = Person("Person", 0, "tired")
    volleyBall = FavoriteHobby("Volley Ball", "A game where a team of players hit a ball over a net.")
    gcis = Course("GCIS-123-16", "Thomas Maszerowski", 30)
    person.favoriteHobby = volleyBall
    person.courses.append(gcis)

    print("Person: %s\n"%person)
    print("Person: name: %s\tmood: %s\tage: %d\thobby: %s\tcourses %s\n"%(person.name, person.mood, person.age, person.favoriteHobby.hobby_name, person.courses[0].course_id))
    
    # Make rit courses
    calculus = Course("MATH-182A", "Chad Gratton", 30)
    csec = Course("CSEC-140", "Sid", 1)

    # Make a dictionary of courses accessed by the course id.
    course_list = dict()
    course_list = {calculus.course_id:calculus, 
                   gcis.course_id:gcis,
                   csec.course_id:csec }

    # Prompt the user for a course id and search the dictionary for the course. Print out the name
    # of the course, the professor, and the number of students in the class
    while(True):
        course_input = input("What course are you taking (course id): ")

        if(course_input == "q"):
            break
        elif (course_input in course_list):
            course = course_list[course_input] 
            print("\tCourse ID: %s\n\tProfessor: %s\n\tNumber of Students: %s\n"%(course.course_id, course.professor, course.number_of_students))

        # find the course from the inputted course_id
        

if __name__ == "__main__":
    main()