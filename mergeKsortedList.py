"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.


Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
"""




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        for i,l in enumerate(lists):
            if l: heappush(h,(l.val,i))

        dummy = curr = ListNode(0)


        while h:
            val,i = heappop(h)
            curr.next = ListNode(val)
            if lists[i].next:
                heappush(h,(lists[i].next.val,i))
                lists[i] = lists[i].next
            curr = curr.next
        return dummy.next         
