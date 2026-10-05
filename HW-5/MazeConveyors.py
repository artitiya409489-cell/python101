from collections import deque

DIRS = {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}
MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def maze_solver_with_conveyors(maze: list[list[str]]) -> dict:
    rows = len(maze)
    cols = len(maze[0]) if rows else 0
    start = end = None

    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'E':
                end = (r, c)

    if start is None or end is None:
        return {"distance": -1, "path": []}

    def inside(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def slide(r, c):
        visited = set()
        cells = []
        while inside(r, c) and maze[r][c] in DIRS:
            if (r, c) in visited:
                return None
            visited.add((r, c))
            cells.append([r, c])
            dr, dc = DIRS[maze[r][c]]
            r, c = r + dr, c + dc
        if not inside(r, c) or maze[r][c] == '#':
            return None
        cells.append([r, c])
        return cells

    parent = {start: None}
    dist = {start: 0}
    queue = deque([start])

    while queue:
        cur = queue.popleft()
        if cur == end:
            break
        r, c = cur
        for dr, dc in MOVES:
            nr, nc = r + dr, c + dc
            if not inside(nr, nc) or maze[nr][nc] == '#':
                continue

            if maze[nr][nc] in DIRS:
                segment = slide(nr, nc)
                if segment is None:
                    continue
            else:
                segment = [[nr, nc]]

            nxt = tuple(segment[-1])
            if nxt not in dist:
                dist[nxt] = dist[cur] + 1
                parent[nxt] = (cur, segment)
                queue.append(nxt)

    if end not in dist:
        return {"distance": -1, "path": []}

    segments = []
    node = end
    while parent[node] is not None:
        prev, seg = parent[node]
        segments.append(seg)
        node = prev

    path = [list(start)]
    for seg in reversed(segments):
        path.extend(seg)

    return {"distance": dist[end], "path": path}


if __name__ == "__main__":
    maze = [
        ['S', '.', '>', '>', 'E'],
        ['#', '#', '#', '#', '#']
    ]
    print(maze_solver_with_conveyors(maze))

    maze = [
        ['S', '.', '>', '#', 'E'],
        ['#', '#', '#', '#', '#']
    ]
    print(maze_solver_with_conveyors(maze))

    maze = [
        ['S', '.', 'v', '.', 'E'],
        ['#', '#', 'v', '.', '#'],
        ['.', '.', 'v', '.', '.'],
        ['#', '#', '.', '.', '#'],
        ['.', '.', '.', '.', '.']
    ]
    print(maze_solver_with_conveyors(maze))