import json
from Elevator import Elevator


class Buildings:
    def __init__(self, filename):
        self.up_elevator = []
        self.down_elevator = []
        try:
            with open(filename, "r") as f:
                self.elevators = []
                j = json.load(f)
                self.minFloor = int(j["_minFloor"])
                self.maxFloor = int(j["_maxFloor"])
                for i in j["_elevators"]:
                    self.elevators.append(Elevator(i))
        except IOError as e:
            print(e)
        self.rest_elevator = [i for i in self.elevators]

    def update_elevator(self, time):
        '''update the pos of evrey elevator'''
        for e in self.up_elevator:
            if e[1] + e[3] - time <= 0:
                e[0].pos = e[2]
                self.rest_elevator.append(e[0])
                self.up_elevator.remove(e)

            else:
                e[1] = e[1] - (time - e[3])
                e[0].pos += e[0].temp_location(time)
                e[3] = time

        for e in self.down_elevator:
            if e[1] + e[3] - time <= 0:
                e[0].pos = e[2]
                self.rest_elevator.append(e[0])
                self.down_elevator.remove(e)
            else:
                e[1] = e[1] - (time - e[3])
                e[3] = time
                e[0].pos -= e[0].temp_location(time)

