class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        counter_for_overlapping=0
        for i, interval1 in enumerate(intervals):

            a1,b1 = interval1

            for j,interval2 in enumerate(intervals):
                if i==j:
                    continue

                a2,b2 = interval2

                if a2 <= a1 and b1 <= b2:
                    counter_for_overlapping +=1
                    break

                    
        return len(intervals) - counter_for_overlapping

        '''
        complexitate


        Complexitate Timp: O(n^2) ca avem O(n) in O(n) de la for in for


        Complexitate Spatiu: O(1) ca nu avem structuri de date ci doar folosim niste variabile
        '''
