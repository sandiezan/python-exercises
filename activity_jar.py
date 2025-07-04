#A replication of my daughter's activity idea jar. The user just needs to decide whether the activity should be indoors or outdoors and the program randomly selects an activity.

import random

indoor_activities = ["Painting",
                     "Playdough",
                     "Play shop",
                     "Play dolls",
                     "Play Santa"]

outdoor_activities = ["Sandpit",
                     "Swing",
                     "Hide and Seek",
                     "Magic potion"]

user_input = input("Would you like an indoor or outdoor activity? ")

if user_input == "indoor":
    print(random.choice(indoor_activities))

else:
    print(random.choice(outdoor_activities))

