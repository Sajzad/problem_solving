"""
Classes
    Median
        - Finding median of two array
    VariableLengthMedian
        - Finding median for unlimited numbers of array

"""


class Median:
    def __init__(self, arr_1, arr_2):
        self.arr_1 = arr_1
        self.arr_2 = arr_2

    def find_median(self):
        print('hello')
        merged_arr = sorted(self.arr_1+self.arr_2)
        print(merged_arr)
        if len(merged_arr) == 1:
            return merged_arr[0]
        elif len(merged_arr)%2!=0:
            return merged_arr[int((len(merged_arr)-1)/2)]
        else:
            index = int((len(merged_arr)-1)/2)
            return (merged_arr[index] + merged_arr[index+1])/2

class VariableLenghtMedian:
    def __init__(self, *arr_1):
        self.arr_1 = arr_1

    def find_median(self):
        merged_arr = []
        for arr in self.arr_1:
            merged_arr = merged_arr+arr
        merged_arr = sorted(merged_arr)
        print(merged_arr)
        if len(merged_arr) == 1:
            return merged_arr[0]
        elif len(merged_arr)%2!=0:
            return merged_arr[int((len(merged_arr)-1)/2)]
        else:
            index = int((len(merged_arr)-1)/2)
            return (merged_arr[index] + merged_arr[index+1])/2


if __name__ == "__main__":

    median_obj = VariableLenghtMedian([1,2],[3,4,33],[0],[11,13,8,4,6])
    print(median_obj.find_median())