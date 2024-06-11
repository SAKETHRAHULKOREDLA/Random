class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=None

def middle_element(head):
    if head is None or head.next is None:
        return head
    temp=head
    count=0
    while temp is not None:
        count+=1
        temp=temp.next
    m=count//2+1
    temp=head
    while temp is not None:
        m=m-1
        if m==0:
            break
        temp=temp.next
    return temp
    
def sum_ll(head):
    x=0
    temp=head
    while temp is not None:
        x+=temp.data
        temp=temp.next
    return x
        



head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

middle=middle_element(head)
print(middle.data)
prt=sum_ll(head)
print(prt.data)


