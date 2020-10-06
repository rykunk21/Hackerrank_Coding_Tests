

def minimumMovement(obstacleLanes):
    car_position = 2
    move = 0
    prev = None
    new_obstacles = []

    for obs in obstacleLanes:
        if obs != prev:
            new_obstacles.append(obs)
            prev = obs

    for i in range(len(new_obstacles)):
        if new_obstacles[i] == car_position:
            move += 1
        elif new_obstacles[i] != car_position:
            continue
        try:
            if car_position == 1:
                if new_obstacles[i + 1] == 2:
                    car_position = 3
                else:
                    car_position = 2
            elif car_position == 2:
                if new_obstacles[i + 1] == 1:
                    car_position = 3
                else:
                    car_position = 1
            elif car_position == 3:
                if new_obstacles[i + 1] == 1:
                    car_position = 2
                else:
                    car_position = 1
        except IndexError:
            break
    return move



obstacleLanes_count = int(input().strip())

obstacleLanes = []

for _ in range(obstacleLanes_count):
    obstacleLanes_item = int(input().strip())
    obstacleLanes.append(obstacleLanes_item)

print(obstacleLanes)
print(minimumMovement(obstacleLanes))


