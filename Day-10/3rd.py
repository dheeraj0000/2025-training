tCase = int(input())
for _ in range(tCase):
    n, m = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    def obstacles_needed(x, y):
        sides_free = (1 if x == 1 or x == n else 0) + (1 if y == 1 or y == m else 0)
        return 4 - sides_free
    obstacles_point1 = obstacles_needed(x1, y1)
    obstacles_point2 = obstacles_needed(x2, y2)
    print(min(obstacles_point1, obstacles_point2))