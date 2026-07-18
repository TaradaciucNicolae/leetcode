class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        q = deque([0])

        visited= set([0])

        while q:
            current_room = q.popleft()

            for key in rooms[current_room]:
                if key not in visited:
                    visited.add(key)
                    q.append(key)

        
        
        return len(visited) == len(rooms)
