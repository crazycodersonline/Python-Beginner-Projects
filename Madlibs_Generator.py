# Mad Libs Generator

loop_counter = 1

max_iterations = 2 # you can generate mad libs 2 times

while (loop_counter <= max_iterations):
    #All the Questions that the program will ask to user
    noun = input("Choose a noun: ")
    p_noun = input("Choose a Plural Noun: ")
    noun2 = input("Choose a Noun: ")
    place = input("Name a place: ")
    adjective = input("Choose an adjective (Describing Word): ")
    noun3 = input("Choose a Noun ")
    #Displays the story based ont User input
    print ("*"*50)
    print ("Be Kind to your", noun, "-footed", p_noun)
    print("For a duck may be somebody's", noun2, ",")
    print("Be kind to your",p_noun, "in",place)
    print("Where weather is always", adjective,".")
    print()
    print ("You may think that is this the", noun3, ",")
    print ("well it is.")
    print ("*"*50)

    #Incrementing the loop for next iteration
    loop_counter  = loop_counter  + 1