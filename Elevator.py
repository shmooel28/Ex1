class Elevator:
    def __init__(self, j):
        self.flag = True
        self.pos = 0
        self.stopTime = float(j["_stopTime"])
        self.startTime = float(j["_startTime"])
        self.speed = float(j["_speed"])
        self.State = 0
        self.TimeForClose = float(j["_closeTime"])
        self.TimeForOpen = float(j["_openTime"])
        self.MaxFloor = float(j["_maxFloor"])
        self.MinFloor = float(j["_minFloor"])
        self.id = int(j["_id"])

    def travel_time(self, src, dest):
        '''return the time that take the elevator from floor a to floor b'''
        lenTravel = abs(src - dest)
        if lenTravel == 0: return 0
        return self.TimeForClose + self.startTime + lenTravel / self.speed + self.stopTime + self.TimeForOpen

    def temp_location(self, time):
        '''return the pos of the elevaor base on the speed of the elevaor and the time that went'''
        return int(self.speed * time)

    def mid_dest_time(self):
        '''return the time for middle stop'''
        return float(self.TimeForClose + self.startTime + self.stopTime + self.TimeForOpen)


