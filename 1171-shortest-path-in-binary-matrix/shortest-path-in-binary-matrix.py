class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # Check if start/end blocked
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1

        # Directions: 8 possible
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0), (1, 1)]
        
        queue = deque()
        queue.append((0, 0, 1))  # (row, col, distance)
        grid[0][0] = 1  # Mark as visited

        while queue:
            r, c, dist = queue.popleft()
            if r == n-1 and c == n-1:
                return dist
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    queue.append((nr, nc, dist + 1))
                    grid[nr][nc] = 1  # Mark as visited
        return -1

        # queue = []
        

        # def get_next_state(point, grid, grid_height, grid_width, visited):
        #     next_states = []
        #     possible_directions = [(-1,0),(-1,-1),(-1,1),(1,-1),(1,0),(0,-1),(0,1),(1,1)]
        #     valid_height = list(range(grid_height))
        #     valid_width = list(range(grid_width))

        #     for pd in possible_directions:
        #         next_state = (point[0]+ pd[0], pd[1]+ point[1])
        #         if next_state in visited:
        #             continue
                
                
        #         if next_state[1] in valid_height and next_state[0] in valid_width:
        #             if grid[next_state[0]][next_state[1]]==0:
                    
        #                 next_states.append(next_state)
        #                 visited.append(next_state)
        #             else:
        #                 continue
        #     return next_states

        # queue.append((0,0, 1))

        # grid_height, grid_width = len(grid), len(grid[0])
        # if grid[grid_height-1][grid_width-1] == 1 or  grid[0][0]==1:
        #     return -1
        # visited = []
        # visited.append((0,0))
        # while queue:
        #     row, column, distance = queue.pop(0)

        #     if row == grid_height-1 and column == grid_width-1:
        #         return distance

        #     next_states =  get_next_state((row, column), grid,grid_height, grid_width, visited)
        #     next_states = [(x[0],x[1], distance+1) for x in next_states]
        #     queue = queue + next_states
        
        # return -1




        