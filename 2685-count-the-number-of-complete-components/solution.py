class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # Construim graful ca adjacency list:
        # fiecare nod va avea lista lui de vecini
        groups = defaultdict(list)

        # Graful este undirected, deci pentru muchia a-b:
        # b este vecin cu a, dar și a este vecin cu b
        for a, b in edges:
            groups[a].append(b)
            groups[b].append(a)

        # Ținem minte nodurile deja vizitate
        visited = set()

        # Aici numărăm câte componente complete găsim
        answer = 0

        # Verificăm toate nodurile de la 0 la n - 1
        # Important: unele noduri pot fi izolate și nu apar în edges
        for node in range(n):

            # Dacă nodul nu a fost vizitat, înseamnă că începe o componentă nouă
            if node not in visited:

                # Pornim BFS din acest nod
                q = deque([node])
                visited.add(node)

                # Numărăm câte noduri are componenta curentă
                nodes_count = 0

                # Numărăm toate legăturile către vecini din componentă
                # Fiecare muchie va fi numărată de 2 ori
                total_neighbor_links = 0

                # Parcurgem toată componenta cu BFS
                while q:
                    curr = q.popleft()

                    # Am găsit încă un nod în componentă
                    nodes_count += 1

                    # Adăugăm câți vecini are nodul curent
                    total_neighbor_links += len(groups[curr])

                    # Vizităm toți vecinii nodului curent
                    for nei in groups[curr]:

                        # Dacă vecinul nu a fost vizitat, îl adăugăm în BFS
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)

                # Pentru că fiecare muchie apare de 2 ori în adjacency list,
                # împărțim la 2 ca să aflăm numărul real de muchii
                actual_edges = total_neighbor_links // 2

                # Dacă o componentă are k noduri,
                # ca să fie completă trebuie să aibă k * (k - 1) / 2 muchii
                needed_edges = nodes_count * (nodes_count - 1) // 2

                # Componenta este completă doar dacă are exact toate muchiile necesare
                if actual_edges == needed_edges:
                    answer += 1

        return answer
