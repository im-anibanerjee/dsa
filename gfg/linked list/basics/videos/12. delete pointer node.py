# delete a node with a pointer given to it
# usually in the problems before we have been given first, last, pos node's
# we have been passing 'head' reference to it
# here we will be passing the pointer reference

class Node:
    def __init__(self, k):
        self.key = k
        self.next = None

def delPointer(ptr):
    temp = ptr.next
    ptr.key = temp.key
    ptr.next = temp.next

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

    delPointer(head.next)
    printLList(head)

if __name__=="__main__":
    main()

'''
delete node pointed to by `ptr` (no access to head).
trick: copy next node's data into ptr, then skip over next node.

before:  10(n1) -> 20(n2) -> 30(n3) -> 40(n4) -> 50(n5)
                                ^ptr

step 1: temp = ptr.next  (temp = n4)
step 2: ptr.key = temp.key (copy 40 into n3)
    10(n1) -> 20(n2) -> 40(n3) -> 40(n4) -> 50(n5)
                            ^ptr    ^temp (dup)

step 3: ptr.next = temp.next (skip n4, n4 is now unreachable)
    10(n1) -> 20(n2) -> 40(n3) -------------> 50(n5)
                            ^ptr

after:   10 -> 20 -> 40 -> 50   (n3 now holds old n4's data, n4 dropped)
'''
