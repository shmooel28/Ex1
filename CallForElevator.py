class CallForElevator:
    def __init__(self, call):
        self.name = call[0]
        self.time = float(call[1])
        self.src = int(call[2])
        self.dest = int(call[3])
        self.state = int(call[4])
        self.elevator_index = int(call[5])

    def callDirection(self):
        '''check if the call is go up or down'''
        flag = True
        if self.src - self.dest < 0:
            flag = False
        return flag


