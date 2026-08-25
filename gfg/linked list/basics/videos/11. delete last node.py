# delete last node of a linked list

class Node:
    def __init__(self, k):
        self.key = k
        self.next = None

def delLast(head):
    if head==None:
        return None

    # if there is only single node, deleteing will return empty LList
    if head.next==None:
        return None

    curr = head
    while curr.next.next!=None:
        curr = curr.next

    curr.next = None
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
    printLList(head)
    print()

    head = delLast(head)
    printLList(head)

if __name__=="__main__":
    main()