"""
Session 11B: Classes
"""

# Make a person class that holds the state for a name, age, and mood
class Person:
    # Default values of class Person
    name = "Name"
    age = 0
    mood = "Meh"
    favoriteHobby = None

# Make a course class that holds the state for course_name, course_number, and number_of_students
# Once you have completed the above step, add a state for courses to the person class

# Make a class for a favorite hobby that has fields for hobby_name and description
# Once you've have completed this step, add a state for favorite hobby to the person class
class FavoriteHobby:
    hobby_name = "hobby"
    description = "description"

def main():
    # instantiate a person class with default values
    person = Person()
    print("Person: %s\n"%person)
    print("Person: name: %s\tmood: %s\tage: %d\n"%(person.name, person.mood, person.age))

    # instantiate the person class with your name, age, and mood
    John = Person()
    John.name = "John"
    John.age = 25
    John.mood = "Happy"

    # make a favorite hobby for John
    favoriteHobby = FavoriteHobby()
    favoriteHobby.hobby_name = "Soccer"
    favoriteHobby.description = "A game where players kick a ball and score goals"
    John.favoriteHobby = favoriteHobby
    print("Person: %s\n"%John)
    print("Person: name: %s\tmood: %s\tage: %d"%(John.name, John.mood, John.age))
    print("\t%s's favorite hobby is %s: %s\n"%(John.name, John.favoriteHobby.hobby_name, John.favoriteHobby.description))

    John.name = "AJ"
    John.age = -4
    John.mood = "DEPRESSED"

    # print the instance of this class. what happens?
    print("Person: %s\n"%John)
    print("Person: name: %s\tmood: %s\tage: %d\n"%(John.name, John.mood, John.age))

    # print the individual fields of the class. what happens?

    # instantiate the course class with the GCIS-123 class information
    # add this course to the person class

    # are there any other courses you know the information for? instantiate it.

    # Create some hobbies and assign people the hobbies
    pass

if __name__ == "__main__":
    main()