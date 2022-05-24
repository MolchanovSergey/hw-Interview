start_list = [2, 7, 11, 15]
target = 26

class Soluttion:

    def __init__(self, nums, target):
        self.nums = nums
        self.target = target


    def twoSum(self):

        for index, value in enumerate(self.nums):
            if value > self.target:
                continue
            for index2, value2 in enumerate(self.nums[:-1]):
                if value2 > self.target:
                    continue
                if target - value == value2:
                    return [index, index2]
if __name__ == '__main__':
    my_soluttion = Soluttion(start_list, target)

    print(my_soluttion.twoSum())