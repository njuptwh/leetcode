# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None or head.next == None:
            return head
        l1 =head
        count = 1
        while l1.next:
            count +=1
            l1 = l1.next
        l1.next =head
        for i in range(count - k%count):    
            l1=l1.next
        l2 = l1.next
        l1.next=None
        return l2
#链表题
#链表 l [1,2,3,4,5]   ：   l.next = [2,3,4,5]
#链表定义时，self.next=None，所以才长度有限