# Car game inspired by Mosh

order = ""
is_started = False

while True:
    order = input().lower()
    if order == "start":
        if is_started:
            print("Car is already started!")
        else:
            print("Car started... Ready to go!")
        is_started = True
    elif order == "stop":
        if not is_started:
            print("Car is already stopped!")
        else:
            print("Car stopped.")
        is_started = False
    elif order == "help":
        print(
        """
type 'start' - to start the car
type 'stop' - to stop the car
type 'quit' - to exit
        """
        )
    elif order == "quit":
        break
    else:
        print('I dont understand that, type "help"')