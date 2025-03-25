started = False
while True:
    command = input(">").lower()
    if command == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
    elif command == "start":
        if started:
            print("Car has already started")
        else:
            started = True
            print("Car is ready to go")
    elif command == "stop":
        if not started:
            print("Car has already stopped")
        else:
            started = False
            print("Car stopped")
    elif command == "quit":
        break
    else:
        print("Invalid command")
