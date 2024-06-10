def count_students_unable_to_eat(students, sandwiches):
    unable_to_eat = 0
    n = len(students)

    while students:
        if students[0] == sandwiches[0]:
            students.pop(0)
            sandwiches.pop(0)
            unable_to_eat = 0  
        else:
            students.append(students.pop(0))
            unable_to_eat += 1
        if unable_to_eat == n:
            return n

    return len(students)
students1 = [1,1,0,0]
sandwiches1 = [0,1,0,1]
print(count_students_unable_to_eat(students1, sandwiches1))  # Output: 0

students2 = [1,1,1,0,0,1]
sandwiches2 = [1,0,0,0,1,1]
print(count_students_unable_to_eat(students2, sandwiches2))  # Output: 3