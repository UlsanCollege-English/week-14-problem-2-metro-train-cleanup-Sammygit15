class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def remove_cars(head, target):
    
    # 1. First skip all leading nodes that match the target
    while head is not None and head.value == target:
        head = head.next

    # If list became empty
    if head is None:
        return None

    # 2. Now head is safe. Use previous + current pointers.
    prev = head
    curr = head.next

    while curr is not None:
        if curr.value == target:
            # Remove curr by skipping it
            prev.next = curr.next
            curr = curr.next
        else:
            prev = curr
            curr = curr.next

    return head


if __name__ == "__main__":
    # Optional manual test
    # Example train: 1 -> 2 -> 2 -> 3, remove cars with ID 2
    n4 = Node(3)
    n3 = Node(2, n4)
    n2 = Node(2, n3)
    n1 = Node(1, n2)

    new_head = remove_cars(n1, 2)
    curr = new_head
    while curr is not None:
        print(curr.value, end=" ")
        curr = curr.next
    print()
