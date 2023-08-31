from math import sqrt, floor

def solution(total_area: int) -> list[int]:
    result = []
    remaining_space = total_area - 0
    while remaining_space > 0:
        square_root = floor(sqrt(remaining_space)) 
        largest_square = square_root ** 2
        remaining_space = remaining_space - largest_square
        result.append(int(largest_square))
    return result

if __name__ == "__main__":
    squares = solution(12)
    assert squares == [9, 1, 1, 1]
    squares = solution(15324)
    assert squares == [15129, 169, 25, 1]