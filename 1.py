def get_distance(start, end):
    # Дистанция считается как манхэттенская, то есть ездить можно только по сетке(дорогам)
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


def find_best_orders(start, end, orders):
    orig_distance = get_distance(start, end)
    recommend_orders = []

    for id, order in enumerate(orders):
        pickup = order[0]
        dropoff = order[1]

        distance_to_pickup = get_distance(start, pickup)
        order_distance = get_distance(pickup, dropoff)
        distance_to_dropoff = get_distance(dropoff, end)

        total_distance = distance_to_pickup + distance_to_dropoff + order_distance
        diff_distance = total_distance - orig_distance

        # если общее расстояние больше изначального более чем в два раза,
        # то такой заказ мы не рекомендуем
        if diff_distance <= orig_distance:
            recommend_orders.append(
                {
                    "id": id,
                    "pickup": order[0],
                    "dropoff": order[1],
                    "total_dist": total_distance,
                    "diff_dist": diff_distance,
                }
            )

    return recommend_orders


def get_coords(s):
    # get coords from line and put in tuples
    x = list(map(int, s.split()))
    start, end = zip(*[iter(x)] * 2)
    return start, end


def main():
    with open("input.txt", "r") as f:
        start, end = get_coords(f.readline())
        num_orders = int(f.readline())

        orders = []
        for _ in range(num_orders):
            pickup, dropoff = get_coords(f.readline())
            orders.append((pickup, dropoff))

    recommend_orders = find_best_orders(start, end, orders)

    with open("output.txt", "w", encoding="utf") as f:
        f.write("Recommmendations:\n")
        for order in recommend_orders:
            f.write(f"Order # {order['id']}\n  from: {order['pickup']}, where: {order['dropoff']} \n")
            f.write(f"  total_dist: {order['total_dist']}, extra_dist: {order['diff_dist']} \n")


if __name__ == "__main__":
    main()
