def execCode(s):
    with open(s, "r") as file:
        exec(file.read())

while True:
    print(
        "1 - Morpion\n" +
        "2 - Snake\n"
    )
    try:
        choice = int(input())
        if choice == 1: 
            execCode("Morpion.py")
        elif choice == 2:
            execCode("Snake.py")
    except Exception as ex:
        print("Exception : " + str(ex))