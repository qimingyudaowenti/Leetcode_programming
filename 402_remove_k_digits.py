"""
给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。

注意:

num 的长度小于 10002 且 ≥ k。
num 不会包含任何前导零。

示例 1 :
输入: num = "1432219", k = 3
输出: "1219"
解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。

示例 2 :
输入: num = "10200", k = 1
输出: "200"
解释: 移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。

示例 3 :
输入: num = "10", k = 2
输出: "0"
解释: 从原数字移除所有的数字，剩余为空就是0。

-----------------------------My-------------------------------------
思路： 
1. 删除某一位，会用该位右边的数字替代，所以要保证删除的那一位比右边的数字大，
   循环判断当前数是否比当前栈顶（pop之后的新栈顶）小。
2. 用栈操作比较简单，从左到右依次入栈，下一个将要进栈的数比栈顶小则栈顶出栈。要确定栈的长度!
待优化：
1. 入栈为0时，可以将栈里的多个非零数都出栈
结果：
56 ms, 在Remove K Digits的Python3提交中击败了89.36% 的用户
--------------------------------------------------------------------

------------------------------Best--------------------------------------
思路：
1. 从左往右，删除比右边那一位大的数，重复这个操作，
   循环判断当前数是否比当前栈顶（pop之后的新栈顶）小。
2. 对结果取前x个数即是结果。
优点：
1. 不考虑栈的长度，只需要对结果取前x个即可。
2. 用string代替list实现栈
------------------------------------------------------------------------
"""


class Solution(object):
    def my_removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        num_length = len(num)

        if k == num_length:
            return '0'
        else:  # k < len(num)

            stack_list = []
            stack_list.append(num[0])
            stack_length = 1
            result_length = num_length - k

            for s in num[1:]:
                # 还有数需要弹出时，循环判断当前数是否比当前栈顶（pop之后的新栈顶）小
                while k != 0 and stack_length != 0 and s < stack_list[-1]:  # 字符串比较大小
                    stack_list.pop()
                    stack_length -= 1
                    k -= 1

                if stack_length < result_length:  # 栈未满，比栈顶大的数也继续添加
                    stack_list.append(s)  
                    stack_length += 1
                else:
                    k -= 1  # 栈满，下一个数未入栈，相当于弹出一个数
                
                if k == 0 and stack_length == result_length:
                    break  # 已经弹出k个数，栈也满了，后面的数就不用考虑了，直接break

            remove_result = ''.join(stack_list).lstrip('0')  # 拼接列表，去除左边的'0'

        return '0' if remove_result == '' else remove_result
    
    def best_removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        res = ''
        n = len(num)
        keep = n - k
        for c in num:
            while k and res and res[-1] > c:
                res = res[:-1]
                k -= 1
            res += c
        print(res)
        while res and res[0] == '0':
            res = res[1:]
        res = res[:keep]
        return res if res else '0'


if __name__ == '__main__':
    my_solution = Solution()
    print(my_solution.best_removeKdigits("123891231233123", 5))
    print(my_solution.best_removeKdigits("5337", 2))
    print(my_solution.best_removeKdigits("222222222222222222222210", 12))
