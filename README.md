# leetcode_practice

自己leetcode练习

# 看了答案的思路才AC的题目
## 符号说明
|题目类型|类型编码|
|-|-|
|数组|0|
|动态规划|1|
|字符串|2|
|树|3|
|哈希表|4|
|贪心|5|
|排序|6|
|双指针|7|
|栈|8|
|堆|9|


|题目级别|类型编号|
|-|-|
|简单|0|
|中等|1|
|困难|2|

## 错题集
|题目类型|题目级别|题目标号|第一次通过时间|第一次使用方法|上次通过时间|上次使用方法|已提交次数|题目链接
|-|-|-|-|-|-|-|-|-|
|1|1|338|2019-12-17|暴力法|2019-12-18|动态规划|2|[链接](https://leetcode-cn.com/problems/counting-bits/)|
|1|1|877|2019-12-18|递归 超时|2019-12-18|动态规划，数学|3|[链接](https://leetcode-cn.com/problems/stone-game/)|
|1|1|1227|2019-12-19|归纳法|2019-12-19|归纳法|1|[链接](https://leetcode-cn.com/problems/airplane-seat-assignment-probability/)|
|1|1|96|2019-12-19|动态规划|2019-12-19|动态规划|1|[链接](https://leetcode-cn.com/problems/unique-binary-search-trees/)|
|2|1|1221|2019-12-24|自己第一直觉 错误|2019-12-24|栈|3|[链接](https://leetcode-cn.com/problems/split-a-string-in-balanced-strings/)|
|3|0|101|2019-12-26|第一次递归没写出来|2019-12-26|递归，两颗树进行比较|2|[链接](https://leetcode-cn.com/problems/symmetric-tree/)|
|3|0|1189|2019-12-26|第一次递归没写出来|2019-12-26|递归，两颗树进行比较|２|[链接](https://leetcode-cn.com/problems/symmetric-tree/)|
|3|0|107|2019-12-29|以前只写过不分层打印的|2019-12-29|只用增加一个队列大小就可以分层打印|２|[链接](https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/)|
|3|0|111|2019-12-29|以为跟求最大深度类似，但是其实并不是，所以错误|2019-12-29|注意边界，考虑完整情况|3|[链接](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree)|
|3|0|112|2019-12-29|不会遍历，不会转化为递归问题|2019-12-29|使用递归解决|2|[链接](https://leetcode-cn.com/problems/path-sum)|
|3|0|235|2020-1-1|递归|2020-1-1|迭代|2|[链接](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)|
|3|0|257|2020-1-1|第一次没思路|2020-1-1|增加path参数|1|[链接](https://leetcode-cn.com/problems/binary-tree-paths/)|
|3|0|113|2020-1-2|写成了局部路径，导致路径输出错误|2020-1-2|修改成全局路径|2|[链接](https://leetcode-cn.com/problems/path-sum-ii/)|
|3|0|543|2020-1-2|通过但是运行时间只超过了10%|2020-1-2|通过一个max变量|2|[链接](https://leetcode-cn.com/problems/diameter-of-binary-tree/)|
|3|0|606|2020-1-3|没思路|2020-1-2|看了解答|2|[链接](https://leetcode-cn.com/problems/subtree-of-another-tree/)|
|3|0|617|2020-1-4|没思路|2020-1-4|递归合并|1|[链接](https://leetcode-cn.com/problems/merge-two-binary-trees/)|
|3|0|653|2020-1-4|未考虑k = 2A的情况|2020-1-4|边建表边查询|1|[链接](https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/)|
|4|0|205|2020-1-9|未考虑某些特殊情况|2020-1-9|转化问题|2|[链接](https://leetcode-cn.com/problems/isomorphic-strings/)|
|4|0|219|2020-1-10|自己思路复杂，超时|2020-1-10|转化问题|2|[链接](https://leetcode-cn.com/problems/contains-duplicate-ii/)|
|4|0|219|2020-1-12|自己思路n^3，超时|2020-1-12|对矩阵元素进行hash|2|[链接](https://leetcode-cn.com/problems/number-of-boomerangs/)|
|4|0|219|2020-1-12|以为必须会死方阵|2020-1-12|每个1的贡献边数|2|[链接](https://leetcode-cn.com/problems/island-perimeter/)|
|5|0|219|2020-1-28|双层循环n^2|2020-1-28|现将所有奇（或偶）数移动到某个奇（或偶）数位，然后再将所有奇数（偶数）移动到偶数（奇数）位置|2|[链接](https://leetcode-cn.com/problems/play-with-chips/)|
|5|0|219|2020-1-28|无思路|2020-1-28|对差进行排序|1|[链接](https://leetcode-cn.com/problems/two-city-scheduling)|
|6|0|219|2020-1-29|无思路|2020-1-29|冒泡排序减少计算量|2|[链接](https://leetcode-cn.com/problems/largest-perimeter-triangle)|
|6|0|219|2020-1-29|找到不同距离的各个点，自己之前焦点在距离，而后面焦点在网格|2020-1-29|开辟一个空间存储不同距离的的点|2|[链接](https://leetcode-cn.com/problems/matrix-cells-in-distance-order)|
|7|0|219|2020-1-30|想着从后面找到第一个不是目标数，替换到当前位置上|2020-1-30|两种简单方法|3|[链接](https://leetcode-cn.com/problems/remove-element)|
|7|0|345|2020-1-31|用空间换时间，用栈来翻转字符|2020-1-31|采用头尾双指针，注意边界条件|4|[链接](https://leetcode-cn.com/problems/reverse-vowels-of-a-string)|
|7|0|141|2020-1-31||2020-1-31|通过双指针判断链表中有没有环|1|[链接](https://leetcode-cn.com/problems/linked-list-cycle)|
|7|0|234|2020-2-1|自己想到复制链表数据到数组中，然后使用双指针判断，但是空间复杂度为O(n)|2020-2-1|通过反转后半部分链表，然后通过两边对比，来判断|2|[链接](https://leetcode-cn.com/problems/palindrome-linked-list)|
|8|0|1021|2020-2-2|无思路|2020-2-2|参考了答案，使用一个变量记录括号的数量|1|[链接](https://leetcode-cn.com/problems/remove-outermost-parentheses/)|
|9|0|703|2020-2-9|采用优先队列存入了所有元素，最后导致一个测试用例超时|2020-2-9|采用堆，只存储k个大小的元素|2|[链接](https://leetcode-cn.com/problems/kth-largest-element-in-a-stream)|