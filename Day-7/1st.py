


def min_time_to_reach_k(A, K):
    deficits = [max(0, K - x) for x in A]
    max_deficit = max(deficits)
    return max_deficit
A = [4,2 ,1]
K = 5
print(min_time_to_reach_k(A, K))