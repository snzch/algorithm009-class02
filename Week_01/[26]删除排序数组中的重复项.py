from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        cur_unique_num_index = 0
        for i in range(1, len(nums)):
            if nums[cur_unique_num_index] != nums[i]:
                cur_unique_num_index += 1
                nums[cur_unique_num_index] = nums[i]
        return cur_unique_num_index + 1


if __name__ == "__main__":
    input_output = [
        [[], 0],
        [[0], 1],
        [[0, 0, 1, 2], 3],
        [[0, 0, 1, 1, 2], 3],
        [[0, 0, 1, 1, 2, 2], 3],
        [[0, 1, 1, 2, 2], 3],
    ]
    solution = Solution()
    for i, o in input_output:
        if solution.removeDuplicates(i) != o:
            print('error: input-{} output-{}'.format(i, o))