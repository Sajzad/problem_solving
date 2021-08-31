"""
Find a number from a given array
    SearchArray
        - find out an element from an array
        Time Complexity
            - O(log2 n)
        Space Complexity
            -O(1)
    SearchValueIndex
        - Find index of an element of an array
        Time Complexity
            - O(n/2)
        Space Complexity
            - O(1)

"""

class SearchArray:
    def __init__(self, arr, target):
        self.arr = arr
        self.target = target

    def find_value(self):
        self.arr = sorted(self.arr)
        for x in range(1,10):
            mid_num = self.arr[int(len(self.arr)/2)]

            print("first",mid_num)
            if self.target == mid_num:
                print("targert number: ",mid_num)
                return mid_num
            elif self.target>mid_num:
                self.arr = self.arr[int(len(self.arr)/2):]
                print(self.arr)
            else:
                self.arr = self.arr[:int(len(self.arr)/2)]
                print(self.arr)

class SearchValueIndex:
    def __init__(self, arr, target):
        self.arr = arr
        self.target = target

    def find_index(self):
        self.arr = sorted(self.arr)
        print(self.arr)
        length = int((len(self.arr)-1)/2)
        print(length)
        # new_len = length
        while True:
            mid_num = self.arr[length]
            print("first",mid_num)
            if self.target == mid_num:
                print("targert number: ",mid_num, length)
                return mid_num
            elif self.target>mid_num:
                length = length+1
                print(length)
            elif self.target<mid_num:
                length = length-1
                print(length)

            else:
                pass

if __name__ == "__main__":
    search_obj = SearchValueIndex([3,2,1,8,99,7,10,15,20,8,45,9,18,19],1)
    search_obj.find_index()