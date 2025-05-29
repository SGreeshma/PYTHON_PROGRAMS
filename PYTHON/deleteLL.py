class Node:
    def __init__(self, data):
        self.val=data
        self.next=None
    def createLL(arr):
        head=None
        for data in arr:
            if (head==None):
                head=Node(data)
                temp=head
            else:
                temp.next=Node(data)
                temp=temp.next
        printLL(head)
def printLL(head):
        temp=head
        while(temp):
             print(temp.val, end=" ")
             temp=temp.next
        return head.val, 
arr=list(map(int, input().split()))
head=Node.createLL(arr)
print(head)