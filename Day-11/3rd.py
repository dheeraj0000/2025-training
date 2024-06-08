#{12,3.45,56,8.90,71}-->true {oddIndex->float,evenIndex}->int
#{0.0,6,7,8.9,60,9.9}->Flase



def check_sequence(sequence):
    for index, value in enumerate(sequence):
        if index % 2 == 0:  # Even index
            if not isinstance(value, int):
                return False
        else:  # Odd index
            if not isinstance(value, float):
                return False
    return True

# Test cases
sequence1 = [12, 3.0, 45, 56.0, 8, 90.0, 71]  # This should print True
sequence2 = [0.0, 6, 7, 8.9, 60, 9.9]         # This should print False
sequence3 = [1, 1.1, 2, 2.2, 3, 3.3]          # This should print True
sequence4 = [1.0, 1, 2.0, 2, 3.0, 3]          # This should print False

print(check_sequence(sequence1))  # Expected output: True
print(check_sequence(sequence2))  # Expected output: False
print(check_sequence(sequence3))  # Expected output: True
print(check_sequence(sequence4))  # Expected output: False
