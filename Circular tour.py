class Solution:
    def tour(self, lis, n):
        total_petrol, total_distance, surplus_petrol, start_index = 0, 0, 0, 0

        for i in range(n):
            petrol, distance = lis[i][0], lis[i][1]
            total_petrol += petrol
            total_distance += distance
            surplus_petrol += petrol - distance

            # If surplus becomes negative, reset starting point and surplus
            if surplus_petrol < 0:
                start_index = i + 1
                surplus_petrol = 0

        # If total petrol is less than total distance, return -1
        if total_petrol < total_distance:
            return -1
        else:
            return start_index