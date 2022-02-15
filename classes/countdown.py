class CountdownHandler:
    from typing import Union
    def __init__(self, time:Union[int, float], playSound:bool=False, soundLoc: str="C:\\Windows\\Media\\Alarm01.wav") -> None:
        """Initializes the CountdownHandler

        Args:
            time (int, Float): The time that the countdown will last for
            playSound (bool, optional): If the program should play a sound when the countdown ends. Defaults to False.
            soundLoc (str, optional): The sound file that should be played when the countdown ends. Defaults to "C:\Windows\Media\Alarm01.wav".
        """

        self.time = time
        self.is_running = False
        self.playSound = playSound
        self.soundLoc = soundLoc
        # check for correct values
        if not self.playSound:
            self.soundLoc == "C:\\Windows\\Media\\Alarm01.wav"
        if not isinstance(self.time, int) and not isinstance(self.time, float):
            # try to swap to int or float
            try:
                self.time = int(self.time)
            except ValueError:
                try:
                    self.time = float(self.time)
                except ValueError as e:
                    raise TypeError("time must be int or float" ) from e


    
    def start(self) -> None:
        """Starts the countdown

        Raises:
            TypeError: Just in case the time is not an integer or float (IMPOSSIBLE)
            FileNotFoundError: If the sound file is not found (only happens if self.playSound = True)
        """

        self.is_running = True
        import time
        if isinstance(self.time, int):
            while self.time > 0:
                time.sleep(1)
                self.time -= 1
                print(self.time, end="\r")
            print("\n")
        elif isinstance(self.time, float):
            while self.time > 0:
                time.sleep(0.1)
                self.time -= 0.1
                self.time = round(self.time, 1)
                print(self.time, end="\r")
            print("\n")
        else:
            raise TypeError("time must be int or float")
        if self.playSound:
            import winsound
            import os
            if os.path.isfile(self.soundLoc):
                winsound.PlaySound(self.soundLoc, winsound.SND_FILENAME)
            else:
                raise FileNotFoundError(f"{self.soundLoc} does not exist")

        self.is_running = False
