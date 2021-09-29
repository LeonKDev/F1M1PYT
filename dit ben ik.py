import datetime 

script = True
while True:
    print("Hello you!, ik ben Leon Kruijer.")
    print("Wie ben jij?")
    username = input("username:")
    print("")
    print("hallo", username)
    print("")
    print("ik ben een nieuwkomer op het mediacollege, met een paar vragen kom je mij beter te leren kennen")
    print("")
    # vraag 1
    answer1 = input("waar woon ik \na. castricum \nb. heerhugowaard \nc. amsterdam \nanswer: ")
    if answer1 == "b" or answer1 == "heerhugowaard" or answer1 == "B":
        print("correct")
        print("\n")
    else:
        print("incorrect! het was B")
        print("\n")
         # vraag 2
    answer2 = input("hoe oud ben ik \na. 16 \nb. 17 \nc. 18 \nanswer:")
    if answer2 == "a" or answer2 == "A" or answer2 == "16":
        print("correct")
        print("\n")
    else:
        print("incorrect! het was A")
        print("\n")
         # vraag 3
    answer3 = input("wat doe ik voor sport \na. basketball \nb. volleybal \nc. workout \nanswer:")
    if answer3 == "C" or answer3 == "c" or answer3 =="workout":
        print("correct")
        print("\n")
    else:
        print("incorrect! het was C")
        print("\n")
         # vraag 4
    answer4 = input("hoe kom ik naar school \na. trein \nb. vliegtuig \nc. fiets \nanswer:")
    if answer4 == "a" or answer4 == "A" or answer4 == "trein":
        print("correct")
        print("\n")
    else:
        print("incorrect! het was A")
        print("\n")
    print("do you want to repeat?")
    inputText = input()
    print("input", inputText)
    print("")
    if inputText == "no": 
        break