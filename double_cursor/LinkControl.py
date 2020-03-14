class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def createLink(data):
    if data==[]:
        return None
    head = ListNode(data[0])
    p = head
    for i in range(1,len(data)):
        tmp = ListNode(data[i])
        p.next = tmp
        p = tmp
    return head

def visitLink(head):
    if not head:
        return
    p = head
    while p:
        print(p.val)
        p = p.next

def reverseVisitLink(head):
    if not head:
        return
    reverseVisitLink(head.next)
    print(head.val)

def reverseLink(head):
    if not head:
        return
    p = head
    previous = None
    while p:
        tmp = p.next
        p.next = previous
        previous = p
        p = tmp
    return previous

head = createLink([1,2,3,4,5])
head = reverseLink(head)
print('顺序访问')
visitLink(head)
print('逆序访问')
reverseVisitLink(head)