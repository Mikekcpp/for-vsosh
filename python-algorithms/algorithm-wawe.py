from collections import deque

def wave_algorithm(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    queue = deque([start])
    distances = [[-1 for _ in range(cols)] for _ in range(rows)]
    distances[start[0]][start[1]] = 0
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0 and distances[nx][ny] == -1:
                distances[nx][ny] = distances[x][y] + 1
                queue.append((nx, ny))
                
                if (nx, ny) == end:
                    return distances
    
    return None  


grid = [
    [0, 0, 0],
    [1, 1, 0],
    [0, 0, 0]
]


start = (0, 0)
end = (2, 2)
distances = wave_algorithm(grid, start, end)

if distances:
    print("Кратчайшее расстояние:", distances[end[0]][end[1]])
else:
    print("Путь не найден.")