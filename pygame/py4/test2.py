def find_shortest_path(matrix, start, end):
    current = end
    path = [current]

    while current != start:
        x, y = current
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        next_val = float('inf')
        next_coord = None

        for neighbor in neighbors:
            nx, ny = neighbor
            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]):
                if matrix[nx][ny] < next_val:
                    next_val = matrix[nx][ny]
                    next_coord = neighbor

        current = next_coord
        path.append(current)

    path.reverse()
    return path


maze = [[7, 6, 5, 6, 7],
        [6, 5, 4, 5, 6],
        [5, 4, 3, 4, 5],
        [4, 3, 2, 3, 4],
        [3, 2, 1, 2, 3]]

start = (4, 2)
end = (0, 4)

shortest_path = find_shortest_path(maze, start, end)
print(shortest_path)