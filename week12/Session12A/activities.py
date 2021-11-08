"""
Session 12A: Classes and constructors
"""

# Make a person class that holds the state for a name, age, and mood
class Person:
    # Default values of class Person
    name = "Name"
    age = 0
    mood = "Meh"
    favoriteHobby = None
    courses = list()

    # Refactor the code so that the person class only accepts use of the variables defined above.

    # Make a constructor for this class

# Make a course class that holds the state for course_name, course_number, and number_of_students
# Once you have completed the above step, add a state for courses to the person class
class Course:
    course_id = "ABC-123"
    professor = "Professor Name"
    number_of_students = 0

    # Refactor the code so that the person class only accepts use of the variables defined above.

    # Make a constructor for this class


# Make a class for a favorite hobby that has fields for hobby_name and description
# Once you've have completed this step, add the state for favorite hobby to the person class
class FavoriteHobby:
    hobby_name = "hobby"
    description = "description"

    # Refactor the code so that the person class only accepts use of the variables defined above.

    # Make a constructor for this class

def main():
    # instantiate a person class with default values
    person = Person()
    print("Person: %s\n"%person)
    print("Person: name: %s\tmood: %s\tage: %d\n"%(person.name, person.mood, person.age))

    # instantiate the course class with the GCIS-123 class information
    # add this course to the person class
    gcis = Course()
    gcis.course_name = "GCIS"
    gcis.course_number = "123"
    gcis.number_of_students = 30

    # instantiate the person class with your name, age, and mood
    John = Person()
    John.name = "John"
    John.age = 25
    John.mood = "Happy"
    John.courses.append(gcis.course_id)

    AJ = Person()
    AJ.name = "AJ"
    AJ.age = -4
    AJ.mood = "DEPRESSED"
    AJ.courses.append(gcis.course_id)

    Zoe = Person()
    Zoe.name = "Zoe"
    Zoe.age = 19
    Zoe.mood = "Tired"

    # Create some hobbies and assign people the hobbies
    # make a favorite hobby for John
    soccer = FavoriteHobby()
    soccer.hobby_name = "Soccer"
    soccer.description = "A game where players kick a ball and score goals"
    John.favoriteHobby = soccer

    # make AJ's favorite hobby
    sleep = FavoriteHobby()
    sleep.hobby_name = "Sleeping"
    sleep.description = "Going to bed"
    AJ.favoriteHobby = sleep
    Zoe.favoriteHobby = sleep


    # print the instance of this class. what happens?
    # print the individual fields of the class. what happens?
    print("Person: %s\n"%John)
    print("Person: name: %s\tmood: %s\tage: %d\tclasses:%s"%(John.name, John.mood, John.age, John.courses))
    print("\t%s's favorite hobby is %s: %s\n"%(John.name, John.favoriteHobby.hobby_name, John.favoriteHobby.description))
    
    print("Person: %s\n"%AJ)
    print("Person: name: %s\tmood: %s\tage: %d\tclasses:%s"%(AJ.name, AJ.mood, AJ.age, AJ.courses))
    print("\t%s's favorite hobby is %s: %s\n"%(AJ.name, AJ.favoriteHobby.hobby_name, AJ.favoriteHobby.description))

    print("Person: %s\n"%Zoe)
    print("Person: name: %s\tmood: %s\tage: %d\tclasses:%s\n"%(Zoe.name, Zoe.mood, Zoe.age, Zoe.courses))
    print("\t%s's favorite hobby is %s: %s\n"%(Zoe.name, Zoe.favoriteHobby.hobby_name, Zoe.favoriteHobby.description))

    # are there any other courses you know the information for? instantiate it.

    # Make a dictionary of courses accessed by the course id.

    # Prompt the user for a course id and search the dictionary for the course. Print out the name
    # of the course, the professor, and the number of students in the class

    pass

if __name__ == "__main__":
    main()