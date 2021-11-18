from Buildings import Buildings
from CallForElevator import CallForElevator
import csv


def read_from_csv(filename):
    with open(filename) as f:
        rows = []
        call = csv.reader(f)
        for row in call:
            if int(row[2]) < buildings.minFloor or int(row[2]) > buildings.maxFloor or int(
                    row[3]) < buildings.minFloor or int(row[3]) > buildings.maxFloor:
                pass
            else:
                rows.append(CallForElevator(row))
    return rows


def write_to_csv(filename_out):
    out_list = []
    for allocate in callList:
        out_list.append(allocate.__dict__.values())
    filename = filename_out
    with open(filename, 'w', newline="") as file:
        csv_write = csv.writer(file)
        csv_write.writerows(out_list)


def clos_to_end(elevator_list):
    '''check the first elevator that and the current call'''
    count = 100
    temp = elevator_list[0]
    for e in elevator_list:
        if e[1] < count:
            count = e[1]
            temp = e
    return temp


def allocate_elevator():
    for c in callList:
        flag = False
        buildings.update_elevator(c.time)
        if len(buildings.rest_elevator) != 0:
            '''check if we have an unused elevator, if have, allocate the closest and fastest elevator'''
            distances = 1000
            for e in buildings.rest_elevator:
                if abs(e.pos - c.src) < distances:
                    temp_rest = e
                    distances = abs(e.pos - c.src)
                else:
                    if abs(e.pos - c.src) == distances:
                        if e.speed > temp_rest.speed:
                            temp_rest = e
            if c.callDirection():
                buildings.up_elevator.append([temp_rest, temp_rest.travel_time(temp_rest.pos, c.src) +
                                              temp_rest.travel_time(c.src, c.dest), c.dest, c.time])
                for e in buildings.rest_elevator:
                    if e.id == temp_rest.id:
                        buildings.rest_elevator.remove(e)
                c.elevator_index = temp_rest.id
            else:
                buildings.down_elevator.append(
                    [temp_rest, temp_rest.travel_time(temp_rest.pos, c.dest) + temp_rest.travel_time(c.src, c.dest),
                     c.dest, c.time])
                for e in buildings.rest_elevator:
                    if e.id == temp_rest.id:
                        buildings.rest_elevator.remove(e)
                c.elevator_index = temp_rest.id
        elif c.callDirection():
            if len(buildings.up_elevator) != 0:
                index = -10000
                temp_speed = 0
                for e in buildings.up_elevator:
                    if e[0].pos < c.src:
                        if e[0].pos > index:
                            if e[0].speed > temp_speed:
                                temp = e
                                temp_speed = e[0].speed
                                index = e[0].pos
                if index != -10000:
                    if temp[2] < c.dest:
                        temp_elevator = buildings.up_elevator.index(temp)
                        buildings.up_elevator[temp_elevator][1] = temp[0].travel_time(temp[0].pos, c.dest) + temp[
                            0].mid_dest_time()
                        buildings.up_elevator[temp_elevator][2] = c.dest
                    else:
                        temp_elevator = buildings.up_elevator.index(temp)
                        buildings.up_elevator[temp_elevator][1] += temp[0].mid_dest_time()
                    c.elevator_index = temp[0].id
                    flag = True
                elif len(buildings.down_elevator) != 0:
                    temp = clos_to_end(buildings.down_elevator)
                    c.elevator_index = temp[0].id
                    buildings.down_elevator.remove(temp)
                    buildings.up_elevator.append(temp)
                else:
                    temp = clos_to_end(buildings.up_elevator)
                    c.elevator_index = temp[0].id
                    buildings.up_elevator.remove(temp)
                    buildings.down_elevator.append(temp)
            elif len(buildings.down_elevator) != 0:
                temp = clos_to_end(buildings.down_elevator)
                c.elevator_index = temp[0].id
                buildings.down_elevator.remove(temp)
                buildings.up_elevator.append(temp)
            else:
                temp = clos_to_end(buildings.up_elevator)
                c.elevator_index = temp[0].id
                buildings.up_elevator.remove(temp)
                buildings.down_elevator.append(temp)

        else:
            if len(buildings.down_elevator) != 0:
                index = 100
                temp_speed = 0
                for e in buildings.down_elevator:
                    if e[0].pos > c.src:
                        if e[0].pos < index:
                            if e[0].speed > temp_speed:
                                temp = e
                                temp_speed = e[0].speed
                                index = e[0].pos
                if index != 100:
                    if temp[2] > c.dest:
                        temp_elevator = buildings.down_elevator.index(temp)
                        buildings.down_elevator[temp_elevator][1] = temp[0].travel_time(temp[0].pos, c.dest) + temp[
                            0].mid_dest_time()
                        buildings.down_elevator[temp_elevator][2] = c.dest
                        c.elevator_index = temp[0].id
                    else:
                        temp_elevator = buildings.down_elevator.index(temp)
                        buildings.down_elevator[temp_elevator][1] += temp[0].mid_dest_time()
                        c.elevator_index = temp[0].id
                else:
                    if len(buildings.up_elevator) != 0:
                        temp = clos_to_end(buildings.up_elevator)
                        c.elevator_index = temp[0].id
                        buildings.up_elevator.remove(temp)
                        buildings.down_elevator.append(temp)
                    else:

                        temp = clos_to_end(buildings.down_elevator)
                        c.elevator_index = temp[0].id
                        buildings.down_elevator.remove(temp)
                        buildings.up_elevator.append(temp)
            else:
                if len(buildings.up_elevator) != 0:
                    temp = clos_to_end(buildings.up_elevator)
                    c.elevator_index = temp[0].id
                    buildings.up_elevator.remove(temp)
                    buildings.down_elevator.append(temp)


def Ex1(filename_building, filename_call, filename_out):
    global buildings, callList
    buildings = Buildings(filename_building)
    callList = read_from_csv(filename_call)
    allocate_elevator()
    write_to_csv(filename_out)


def main():
    Ex1("Ex1_input/Ex1_Buildings/B1.json", "Ex1_input/Ex1_Calls/Calls_a.csv", "test_out.csv")


if __name__ == '__main__':
    main()
