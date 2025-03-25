while True:
    command = input(">").lower()
    if command == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
    elif command == "start":
        print("Car is ready to go")
    elif command == "stop":
        print("Car stopped")
    elif command == "quit":
        break
    else:
        print("Invalid command")
