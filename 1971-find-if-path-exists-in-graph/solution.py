class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(list)


            # Exemplu:
            # edges = [[0, 1], [0, 2]]
            # graph[0] = [1, 2]
            # graph[1] = [0]
            # graph[2] = [0]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # Queue pentru BFS.
        # Începem explorarea de la nodul source.
        q = deque([source])

        # Set cu nodurile deja vizitate.
        # Punem source aici de la început ca să nu îl adăugăm din nou.
        visited = set([source])

        while q: # cat timp q nu e gol

            node = q.popleft()

            if node == destination:
                return True
            
            for nei in graph[node]:  # pt graph[0] = [1, 2]  va avea 2 iteratii 
                                    # in care nei e 1 si apoi 2
                if nei not in visited:
                    visited.add(nei)

                    # Îl adăugăm în queue ca să îi explorăm și lui vecinii mai târziu.
                    q.append(nei)

        # Dacă queue-ul s-a golit și nu am găsit destination,
        # înseamnă că nu există drum între source și destination.
        return False
