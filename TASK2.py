#!/usr/bin/env python
# coding: utf-8

# In[3]:


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    dummy = ListNode(0)  # Create a dummy node to serve as the head of the result linked list
    curr = dummy  # Pointer to track the current node in the result linked list
    carry = 0  # Initialize the carry to 0

    while l1 or l2 or carry:
        # Calculate the sum of the current digits and the carry
        sum = carry

        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next

        # Update the carry and create a new node with the sum % 10 as its value
        carry = sum // 10
        curr.next = ListNode(sum % 10)
        curr = curr.next

    return dummy.next  # Return the next node after the dummy node, which is the head of the result linked list


# In[ ]:




