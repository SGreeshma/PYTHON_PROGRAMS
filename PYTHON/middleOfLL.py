# MIDDLE OF THE LINKED LIST
class Node: # node creation
    def __init__(self, data):
        self.data=data
        self.next=None
    def createLL(arr): # nodes linking
        head=None # at initial there will be no nodes
        for data in arr:
            if (head==None): 
                head=Node(data) 
                temp=head
            else:
                temp.next=Node(data)
                temp=temp.next
        #printLL(head)
        middleNode=getMiddle(head) 
        print(middleNode)
def getMiddle(head):
    slow=head
    fast=head
    prev=None
    while(fast and fast.next):
        slow=slow.next
        fast=fast.next.next
        prev=slow
    prev.next=slow.next
    slow.next=None
    return slow.data
def printLL(head): # printing linked list
    temp=head
    while(temp):
        print(temp.data, end=' ')
        temp=temp.next
arr=list(map(int, input().split()))
head=Node.createLL(arr)
printLL(head)