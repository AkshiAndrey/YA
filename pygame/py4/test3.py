import heapq

def astar_search(grid, start, end):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def in_bounds(pos):
        return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])

    def neighbors(pos):
        row, col = pos
        candidates = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        return [(r, c) for r, c in candidates if in_bounds((r, c))]

    start_node = (heuristic(start, end), 0, start, [])
    heap = [start_node]
    visited = set()

    while heap:
        _, cost, current, path = heapq.heappop(heap)

        if current == end:
            return path + [current]

        if current in visited:
            continue

        visited.add(current)

        for neighbor in neighbors(current):
            new_cost = cost + grid[neighbor[0]][neighbor[1]]
            new_node = (new_cost + heuristic(neighbor, end), new_cost, neighbor, path + [current])
            heapq.heappush(heap, new_node)

    return None

grid = [
    [5, 4, 3, 2, 1],
    [6, 5, 4, 3, 2],
    [7, 6, 5, 4, 3],
    [8, -1, -1, -1, -1],
    [9, 10, 11, 12, 13]
]

start = (4, 4)
end = (0, 4)

path = astar_search(grid, start, end)
print(path)