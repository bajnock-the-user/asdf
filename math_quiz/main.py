import math

def feladat_1():
    # Feladat 1: Vonat és alagút
    tunnel_length = 300  # alagút hossza
    time_in_tunnel = 20  # másodperc
    lamp_time = 5  # másodperc

    # Vonat sebessége
    speed = tunnel_length / time_in_tunnel  # m/s

    # A lámpa 5 másodpercig van a vonat felett
    train_length = speed * lamp_time

    print("1:", int(train_length))

def feladat_2():
    # Feladat 2: Marcipánkockák
    # Kockák méretei
    sides = [2, 6, 8]

    # Legnagyobb térfogat
    max_volume = max(s**3 for s in sides)

    print("2:", max_volume)

def feladat_3():
    # Feladat 3: Jancsi és Juliska biciklivel
    # Sebességek km/h
    j_walk = 5
    j_bike = 12
    g_walk = 4
    g_bike = 10

    # Távolság km-ben
    distance = 20

    # Idők kiszámítása
    t_g_total = distance / g_walk
    t_j_bike = distance / j_bike

    # Idő a gyaloglásra
    t_j_walk = t_g_total - t_j_bike

    # Távolság biciklizéssel
    d_j_walk = j_walk * t_j_walk

    print("3:", round(d_j_walk, 2))

def feladat_4():
    # Feladat 4: Kör és rácspontok
    radius = 5
    grid_points = 0

    for x in range(-radius, radius + 1):
        for y in range(-radius, radius + 1):
            if x**2 + y**2 == radius**2:
                grid_points += 1

    print("4:", grid_points)

def feladat_5():
    # Feladat 5: Háromszög területe
    # A háromszög csúcspontjai: A(0, 4), B(3, 0), C(c, 6)
    area = 7

    # Terület kiszámítása
    c = (2 * area) / 3

    print("5:", round(c, 2))

def feladat_6():
    # Feladat 6: Paintball ütközet
    max_people_targeting = 2

    print("6:", max_people_targeting)

def feladat_7():
    # Feladat 7: Golyók
    total_balls = 30
    max_greens = 21  # legalább 21 golyó esetén biztosan van zöld

    red_balls = total_balls - max_greens

    print("7:", red_balls)

def feladat_8():
    # Feladat 8: Négyzetek átlói
    total_diagonal_area = 85  # négyzetcentiméter
    side_length = int(math.sqrt(total_diagonal_area))

    large_square_area = side_length ** 2

    print("8:", large_square_area)

def feladat_9():
    # Feladat 9: Elköszönés
    goodbyes = 198
    viszlats = 308

    # Egyenletek: x * (x + y - 1) = 198, y * (x + y - 1) = 308
    # Oldjuk meg az egyenleteket
    for x in range(1, goodbyes + 1):
        y = (goodbyes + viszlats + 2 - x - x) // 2
        if x * (x + y - 1) == goodbyes and y * (x + y - 1) == viszlats:
            english_participants = x
            break

    print("9:", english_participants)

if __name__ == "__main__":
    feladat_1()
    feladat_2()
    feladat_3()
    feladat_4()
    feladat_5()
    feladat_6()
    feladat_7()
    feladat_8()
    feladat_9()
