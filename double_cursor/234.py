# Definition for singly-linked list.
# 判断链表是否是回文，这个方法是O(n)时间O(1)空间
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        end_of_first_half = self.the_end_of_first_half(head)
        second_begin = self.reverseList(end_of_first_half.next)
        first_begin = head
        while first_begin and second_begin:
            if first_begin.val == second_begin.val:
                first_begin = first_begin.next
                second_begin = second_begin.next
            else:
                return False
        end_of_first_half.next = self.reverseList(second_begin)
        return True

    # 找到链表中的中间节点
    def the_end_of_first_half(self,head):
        fast = head
        slow = head
        while fast.next and fast.next.next: # fast.next 不可以省略，因为有可能fast.next是空，会导致fast.next.next无意义
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self,head):
        previous = None
        current = head
        while current is not None:
            tmp = current.next
            current.next = previous
            previous = current
            current = tmp
        return previous