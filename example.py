from classes.countdown import CountdownHandler

time = input("Enter the time for the countdown to wait: ")
shouldsfx = input("Should the countdown play a sound? (y/n): ")
if shouldsfx == "y":
    shouldsfx = True
    sfx = input("Enter the sound file to play: ") 
else:
    print("No sound will be played.")
    shouldsfx = False
    sfx = None


countdown = CountdownHandler(time, shouldsfx, sfx)
countdown.start()

if countdown.is_running == False:
    print("Countdown finished")