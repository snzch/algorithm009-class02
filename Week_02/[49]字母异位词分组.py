# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
#
#  示例:
#
#  输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
#
#  说明：
#
#
#  所有输入均为小写字母。
#  不考虑答案输出的顺序。
#
#  Related Topics 哈希表 字符串


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
import collections


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            d[key].append(s)
        return list(d.values())
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    input_output = [
        [
            ['qwe', 'ewq', '', '123', '^&*', '*&1', '^&*'],
            [
                ['qwe', 'ewq'],
                [''],
                ['123'],
                ['^&*', '^&*'],
                ['*&1']
            ]
        ],
        [
            [],
            []
        ]
    ]
    solution = Solution()
    for i, o in input_output:
        res = solution.groupAnagrams(i)
        if sorted([sorted(_) for _ in res]) != sorted([sorted(_) for _ in o]):
            print('error')