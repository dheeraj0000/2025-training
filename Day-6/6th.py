def can_reorder_trucks(n, sequence):
    side_street = []
    expected = 1

    for truck in sequence:
        while side_street and side_street[-1] == expected:
            side_street.pop()
            expected += 1

        if truck == expected:
            expected += 1
        else:
            side_street.append(truck)

    while side_street and side_street[-1] == expected:
        side_street.pop()
        expected += 1

    return expected == n + 1

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    while index < len(data):
        n = int(data[index])
        if n == 0:
            break
        index += 1
        sequence = list(map(int, data[index:index + n]))
        index += n
        
        if can_reorder_trucks(n, sequence):
            print("yes")
        else:
            print("no")

if __name__ == "__main__":
    main()
