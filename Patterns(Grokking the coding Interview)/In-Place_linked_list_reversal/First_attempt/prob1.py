from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse_alternate_k_elements(head, k):
    # TODO: Write your code here
    current, prev = head, None

    while True:
        end_prev_part = prev
        end_sub_list = current

        i, _next = 0, None

        while current and i < k:
            _next = current.next
            current.next = prev
            prev = current
            current = _next
            i += 1
        
        if end_prev_part:
            end_prev_part.next = prev
        else:
            head = prev
        
        end_sub_list.next = current

        i = 0

        while current and i < k:
            prev = current
            current = current.next
            i += 1

        if current is None:
            break

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_alternate_k_elements(head, 2)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
