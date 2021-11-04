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
# Once you've have completed this step, add the state for favorite hobby to the person class
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
    soccer = FavoriteHobby()
    soccer.hobby_name = "Soccer"
    soccer.description = "A game where players kick a ball and score goals"
    John.favoriteHobby = soccer
    print("Person: %s\n"%John)
    print("Person: name: %s\tmood: %s\tage: %d"%(John.name, John.mood, John.age))
    print("\t%s's favorite hobby is %s: %s\n"%(John.name, John.favoriteHobby.hobby_name, John.favoriteHobby.description))

    AJ = Person()
    AJ.name = "AJ"
    AJ.age = -4
    AJ.mood = "DEPRESSED"


    Zoe = Person()
    Zoe.name = "Zoe"
    Zoe.age = 19
    Zoe.mood = "Tired"


    # make AJ's favorite hobby
    sleep = FavoriteHobby()
    sleep.hobby_name = "Sleeping"
    sleep.description = "Going to bed"

    # change the state of AJ's hobby to his hobby
    AJ.favoriteHobby = sleep
    print("\t%s's favorite hobby is %s: %s\n"%(AJ.name, AJ.favoriteHobby.hobby_name, AJ.favoriteHobby.description))

    # print the instance of this class. what happens?
    Zoe.favoriteHobby = sleep
    print("Person: %s\n"%Zoe)
    print("Person: name: %s\tmood: %s\tage: %d\n"%(Zoe.name, Zoe.mood, Zoe.age))
    print("\t%s's favorite hobby is %s: %s\n"%(Zoe.name, Zoe.favoriteHobby.hobby_name, Zoe.favoriteHobby.description))


    # print the individual fields of the class. what happens?

    # instantiate the course class with the GCIS-123 class information
    # add this course to the person class

    # are there any other courses you know the information for? instantiate it.

    # Create some hobbies and assign people the hobbies
    pass

if __name__ == "__main__":
    main()