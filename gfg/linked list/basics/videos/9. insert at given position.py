# insert at a given position in a linked list

class Node:
    def __init__(self, k):
        self.key = k
        self.next = None

def insPos(head, k, pos):
    temp = Node(k)

    # if empty
    if head==None:
        return None
    
    if pos==1:
        temp.next = head
        return temp

    else:
        curr = head
        # curr = head, which is already sitting at position 1
        for i in range(1, pos-1):
            curr = curr.next
        
        temp.next = curr.next
        curr.next = temp
        return head

def printLList(head):
    curr = head
    while curr!=None:
        print(curr.key)
        curr = curr.next

def main():
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)

    head = insPos(head, k=15, pos=2)
    printLList(head)

if __name__=="__main__":
    main()