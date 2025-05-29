# LENGTH OF THE LOOP IN LINKED LIST

class Node:
    def __init__(self, data=0, next=None):
        self.val = data
        self.next = next

def lengthOfLoop(head):
    slow=head
    fast=head
    while(fast and fast.next):
        slow=slow.next
        fast=fast.next.next
        if(slow==fast):
            slow=head
            while(slow!=fast):
                slow=slow.next
                fast=fast.next
            c=1
            slow=slow.next
            while(slow!=fast):
                slow=slow.next
                c+=1
            return c
    return 0