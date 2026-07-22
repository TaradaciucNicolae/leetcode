from typing import List
from bisect import bisect_right, bisect_left

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        max_active_s = []
        total_ones = s.count("1")
        n = len(s)

        # RLE pe tot s: [start, end, char, length]
        list_of_s = []
        counter = 1
        current = s[0]

        for i in range(1, n):
            if s[i] == current:
                counter += 1
            else:
                list_of_s.append([i - counter, i - 1, current, counter])
                current = s[i]
                counter = 1

        list_of_s.append([n - counter, n - 1, current, counter])

        # Salvăm doar block-urile de 1 care au 0 în stânga și 0 în dreapta
        starts = []
        ends = []
        left_zero_starts = []
        right_zero_ends = []
        full_gains = []

        for i in range(1, len(list_of_s) - 1):
            if (
                list_of_s[i][2] == "1"
                and list_of_s[i - 1][2] == "0"
                and list_of_s[i + 1][2] == "0"
            ):
                starts.append(list_of_s[i][0])
                ends.append(list_of_s[i][1])
                left_zero_starts.append(list_of_s[i - 1][0])
                right_zero_ends.append(list_of_s[i + 1][1])
                full_gains.append(list_of_s[i - 1][3] + list_of_s[i + 1][3])

        # Construim un segment tree peste full_gains.
        #
        # Il folosim deoarece pentru un query [l, r], pot exista mai multe block-uri de 1 valide.
        # Avem nevoie de cel mai mare gain dintre ele.
     
        # Segment tree-ul ne permite să aflăm: max(full_gains[left : right + 1])


        m = len(full_gains)

        # size va fi prima putere a lui 2 >= m.
        # Folosim asta ca să fie segment tree-ul ușor de construit.
        size = 1
        while size < m:
            size *= 2

        # seg va ține tree-ul.
        # Frunzele încep de la indexul "size".
        seg = [0] * (2 * size)

        # Punem valorile originale full_gains în frunze.
        #
        # Exemplu:
        # full_gains = [3, 5, 2]
        # size = 4
        #
        # seg[4] = 3
        # seg[5] = 5
        # seg[6] = 2
        # seg[7] = 0

        for i in range(m):
            seg[size + i] = full_gains[i]

        # Construim nodurile interne.
        #
        # Fiecare nod ține maximul dintre cei doi copii ai lui.
        #
        # seg[i] = max(seg[2*i], seg[2*i+1])
        #
        # La final, seg[1] este maximul din tot full_gains.
        for i in range(size - 1, 0, -1):
            seg[i] = max(seg[2 * i], seg[2 * i + 1])


        # Procesăm fiecare query.


        for l, r in queries:

            # Pentru ca un block de 1 să fie valid în query [l, r],
            # trebuie să fie complet în interiorul query-ului.
            #
            # Condițiile sunt:
            #
            # start > l
            # end < r
            #
            # De ce strict?
            #
            # Pentru că substring-ul este augmentat cu "1" la ambele capete.
            # Dacă block-ul de 1 atinge marginea query-ului, atunci se lipește
            # de acel "1" artificial și nu mai este surrounded by 0s.
            #
            # A = primul candidat cu start > l
            # B = ultimul candidat cu end < r

            A = bisect_right(starts, l)
            B = bisect_left(ends, r) - 1

            # Dacă nu există niciun candidat valid, nu putem face trade.
            if A > B:
                max_active_s.append(total_ones)
                continue

            best_gain = 0

            # --------------------------------------------------------
            # Candidatul A poate fi "tăiat" de marginea stângă a query-ului.
            #
            # Exemplu:
            #
            # zero-block global:    00000
            # query începe aici:      ^
            #
            # Nu putem folosi tot zero-block-ul din stânga,
            # ci doar partea aflată în query.
            # --------------------------------------------------------

            left_gain = starts[A] - max(l, left_zero_starts[A])
            right_gain = min(r, right_zero_ends[A]) - ends[A]
            best_gain = max(best_gain, left_gain + right_gain)

            # --------------------------------------------------------
            # Candidatul B poate fi "tăiat" de marginea dreaptă a query-ului.
            #
            # Dacă A == B, este același candidat, deci nu-l calculăm de două ori.
            # --------------------------------------------------------

            if B != A:
                left_gain = starts[B] - max(l, left_zero_starts[B])
                right_gain = min(r, right_zero_ends[B]) - ends[B]
                best_gain = max(best_gain, left_gain + right_gain)

            # --------------------------------------------------------
            # Candidații dintre A și B nu sunt tăiați de marginile query-ului.
            #
            # Deci pentru ei putem folosi direct full_gains.
            #
            # Avem nevoie de:
            #
            # max(full_gains[A + 1 : B])
            #
            # adică indici de la A + 1 până la B - 1.
            #
            # Asta este partea unde folosim segment tree-ul.
            # --------------------------------------------------------

            left = A + 1
            right = B - 1

            if left <= right:
                # Mutăm left și right la pozițiile frunzelor din segment tree.
                left += size
                right += size

                # Căutăm maximul pe intervalul [left, right].
                while left <= right:

                    # Dacă left este copil drept, înseamnă că segmentul lui
                    # este complet inclus în intervalul nostru.
                    if left % 2 == 1:
                        best_gain = max(best_gain, seg[left])
                        left += 1

                    # Dacă right este copil stâng, segmentul lui este complet
                    # inclus în intervalul nostru.
                    if right % 2 == 0:
                        best_gain = max(best_gain, seg[right])
                        right -= 1

                    # Urcăm la părinți.
                    left //= 2
                    right //= 2

            # Răspunsul este:
            #
            # numărul inițial de 1-uri din tot s
            # +
            # cel mai bun gain obținut în query
            max_active_s.append(total_ones + best_gain)

        return max_active_s
