
def largest_3x3_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    max_sum = float("-inf")
    
    for i in range(rows - 2):
        for j in range(cols - 2):
            cur_sum = 0
            for x in range(i, i+3):
                for y in range(j, j+3):
                    cur_sum += matrix[x][y]
            
            max_sum = max(max_sum, cur_sum)
    
    return max_sum

matrix = [
    [1,2,0,3],
    [4,5,6,1],
    [7,8,9,4],
    [2,3,1,0]
]

print(largest_3x3_sum(matrix))