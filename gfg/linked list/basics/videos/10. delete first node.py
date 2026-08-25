# delete first node of a linked list

class Node:
    def __init__(self, k):
        self.key = k
        self.next = None

def delFirst(head):
    if head==None:
        return None

    return head.next

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

    head = delFirst(head)
    printLList(head)

if __name__=="__main__":
    main()