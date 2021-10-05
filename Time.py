 class Time:
    def __init__(self, h, m, s):
        while m >= 60 or s >= 60:   # while the format is incorrect
            if s >= 60: # if there are too many seconds
                s -= 60
                m += 1
            if m >= 60: # if there are too many minutes
                m -= 60
                h += 1

        self.__hours = h
        self.__minutes = m
        self.__seconds = s

    def getHours(self):
        return self.__hours

    def getMinutes(self):
        return self.__minutes

    def getSeconds(self):
        return self.__seconds

    def toString(self):
        return str(self.__hours) + ":" + str(self.__minutes) + ":" + str(self.__seconds)

    """
    this method find the total seconds of the Time object
    
    return: returns the value of the object as an int of seconds
    """
    def timeInSeconds(self):
        return self.__hours * 3600 + self.__minutes * 60 + self.__seconds

    """
    this method changes the time
    
    h: the new hours value
    m: the new minutes value
    s: the new seconds value
    """
    def changeTheTime(self, h, m, s):
        self.__hours = h
        self.__minutes = m
        self.__seconds = s

    """
    this method will reformat the Time into a 12 hour clock with am/pm references
    
    return: returns the time but changed into the 12 hour format
    """
    def twelveHourClock(self):
        if self.__hours == 0:  # if it is midnight
            return "12:" + str(self.__minutes) + ":" + str(self.__seconds) + " am"
        elif self.__hours < 12:   # if it is morning
            return self.toString() + " am"
        elif self.__hours == 12:    # if it is noon
            return self.toString() + " pm"
        else:   # if it is afternoon
            return str(self.__hours - 12) + ":" + str(self.__minutes) + ":" + str(self.__seconds) + " pm"

    """
    this method finds the general term for describing the Time
    
    return: returns either morning, afternoon, evening, or nighttime based on the Time
    """
    def whatTimeIsIt(self):
        if self.__hours < 6 or self.__hours > 22:  # if it is nighttime
            return "nighttime"
        if self.__hours < 12:   # if it is the morning
            return "morning"
        elif self.__hours < 17:  # if it is the afternoon
            return "afternoon"
        else:    # if it is the evening
            return "evening"

    """
    this method compares the Time object that called the method with the parameter Time object
    
    return: returns the difference between the two times in seconds
    """
    def compareTo(self, t):
        return self.timeInSeconds() - t.timeInSeconds()

    """
    This method finds the time till the parameter Time object from the object that called the method
    
    return: returns a new Time object representing the time till the parameter Time object
    """
    def timeTill(self, t):
        return Time(0, 0, t.compareTo(self))


