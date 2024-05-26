def solve_problem_1():
    # Vonat hosszának kiszámítása
    tunnel_length = 300  # méter
    total_time = 20  # másodperc
    lamp_time = 5  # másodperc

    # Vonat sebessége
    speed = tunnel_length / total_time  # m/s

    # Vonat hossza
    train_length = speed * lamp_time
    return train_length

def solve_problem_2():
    # Legnagyobb marcipántégla térfogatának kiszámítása
    dimensions = [2, 6, 8]
    dimensions.sort(reverse=True)
    volume = dimensions[0] * dimensions[1] * 2
    return volume

def solve_problem_3():
    # Jancsi és Juliska biciklizési távolsága
    distance_total = 20
    jancsi_walk_speed = 5
    jancsi_bike_speed = 12
    juliska_walk_speed = 4
    juliska_bike_speed = 10
    
    # Átlagos sebesség kiszámítása
    x = (distance_total / (1/jancsi_bike_speed + 1/juliska_bike_speed - 1/jancsi_walk_speed - 1/juliska_walk_speed))
    juliska_bike_distance = (distance_total - x) / (juliska_walk_speed / juliska_bike_speed + 1)
    return juliska_bike_distance

def solve_problem_4():
    # Körvonalon lévő rácspontok száma
    radius = 5
    points = 0
    for x in range(-radius, radius + 1):
        for y in range(-radius, radius + 1):
            if x**2 + y**2 == radius**2:
                points += 1
    return points

def solve_problem_5():
    # Háromszög területe és c meghatározása
    area = 7
    A = (0, 4)
    B = (3, 0)
    
    c_values = [i for i in range(1, 3)]
    for c in c_values:
        if abs(0 * (0 - 6) + 3 * (6 - 4) + c * (4 - 0)) / 2 == area:
            return c
    return None

def solve_problem_6():
    # Legfeljebb hányan lőhetnek ugyanarra az emberre
    return 2

def solve_problem_7():
    # Piros golyók száma
    total_balls = 30
    required_for_three_colors = 23
    required_for_one_color = 21
    blue_and_green = required_for_three_colors - required_for_one_color
    red = total_balls - required_for_three_colors + blue_and_green
    return red

def solve_problem_8():
    # Nagy négyzet területe
    diagonal_area = 85
    side_length = int((diagonal_area * 2) ** 0.5)
    return side_length ** 2

def solve_problem_9():
    # Angol résztvevők száma
    total_goodbyes = 198
    total_viszlats = 308
    
    english = total_goodbyes // 11
    return english

if __name__ == "__main__":
    print("1.:", solve_problem_1())
    print("2.:", solve_problem_2())
    print("3.:", solve_problem_3())
    print("4.:", solve_problem_4())
    print("5.:", solve_problem_5())
    print("6.:", solve_problem_6())
    print("7.:", solve_problem_7())
    print("8.:", solve_problem_8())
    print("9.:", solve_problem_9())
