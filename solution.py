from typing import TypeVar  # For use in type hinting

#Type declarations
T = TypeVar('T')        # generic type
SLL = TypeVar('SLL')    # forward declared Singly Linked List type
Node = TypeVar('Node')  # forward declared Node type


class SLLNode:
    """
    Node implementation
    Do not modify
    """

    __slots__ = ['data', 'next']

    def __init__(self, data: T, next: Node = None) -> None:
        """
        Initialize an SLL Node
        :param data: data value held by the node
        :param next: reference to the next node in the SLL
        :return: None
        """
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """
        Overloads `str()` method, casts SLL nodes to strings
        :return: string representation of node
        """
        return '(Node: ' + str(self.data) + ' )'

    def __repr__(self) -> str:
        """
        Overloads `repr()` method for use in debugging
        :return: string representation of node
        """
        return '(Node: ' + str(self.data) + ' )'

    def __eq__(self, other: Node) -> bool:
        """
        Overloads `==` operator to compare nodes
        :param other: right operand of `==`
        :return: True if the nodes are ==, else False
        """
        return self is other if other is not None else False


class SinglyLinkedList:
    """
    SLL implementation
    """

    __slot__ = ['head', 'tail']

    def __init__(self) -> None:
        """
        Initializes an SLL
        return: None
        DO NOT MODIFY THIS FUNCTION
        """
        self.head = None
        self.tail = None

    def __repr__(self) -> str:
        """
        Represents an SLL as a string
        DO NOT MODIFY THIS FUNCTION
        :return: string representation of SLL
        """
        return self.to_string()

    def __eq__(self, other: SLL) -> bool:
        """
        Overloads `==` operator to compare SLLs
        :param other: right operand of `==`
        :return: True if equal, else False
        DO NOT MODIFY THIS FUNCTION
        """
        comp = lambda n1, n2: n1 == n2 and (comp(n1.next, n2.next) if (n1 and n2) else True)
        return comp(self.head, other.head)

    # ========== Modify below ========== #

    def append(self, data: T) -> None:
        """
        Append an SLLNode to the end of the SLL
        :param data: data to append
        :return: None
        """
        if self.head is None:
            self.head = SLLNode(data)
            self.tail = self.head
        else:
            new = SLLNode(data)
            self.tail.next = new
            self.tail = new


    def to_string(self) -> str:
        """
        Converts an SLL to a string
        :return: string representation of SLL
        """
        if not self.head:
            return "None"
        else:
            res = ""
            temp = self.head
            while temp:
                res += str(temp.data)
                if temp.next:
                    res += " --> "
                temp = temp.next
        return res


    def length(self) -> int:
        """
        Determines number of nodes in the list
        :return: number of nodes in list
        """
        if not self.head:
            return 0
        length = 0
        temp = self.head
        while temp:
            length += 1
            temp = temp.next
        return length


    def total(self) -> T:
        """
        Sums up the values in the list
        :return: total sum of values in the list
        """
        total = None
        if not self.head:
            return None
        temp = self.head
        while temp:
            if total is None:
                total = temp.data
                temp = temp.next
            else:
                total += temp.data
                temp = temp.next
        return total

    def delete(self, data: T) -> bool:
        """
        Deletes the first node containing `data` from the SLL
        :param data: data to remove
        :return: True if a node was removed, else False
        """
        if not self.head:
            return False
        if self.head.data == data:
            if self.head == self.tail:
                self.head = self.head.next
                self.tail = self.head
                return True

            self.head = self.head.next

            return True
        prev = self.head
        temp = self.head.next
        while temp:
            if temp == self.tail and temp.data == data:
                self.tail = prev
                prev.next = None
                return True
            if temp.data != data:
                prev = temp
                temp = temp.next

            else:
                prev.next = temp.next
                return True
        return False

    def delete_all(self, data: T) -> bool:
        """
        Deletes all instances of a node containing `data` from the SLL
        :param data: data to remove
        :return: True if a node was removed, else False
        """
        count = 0
        if not self.head:
            return False
        while self.head and self.head.data == data:
            if self.tail is self.head:
                self.tail = None
            self.head = self.head.next
            count += 1

        if not self.head or not self.head.next:
            return count != 0
        else:
            prev = self.head
            temp = self.head.next
        while temp:
            if temp.data == data:
                if temp == self.tail:
                    self.tail = prev
                    prev.next = None
                    count += 1
                    break
                else:
                    prev.next = prev.next.next
                    count += 1
            prev = temp
            temp = temp.next
        return count != 0


    def find(self, data: T) -> bool:
        """
        Looks through the SLL for a node containing `data`
        :param data: data to search for
        :return: True if found, else False
        """
        if not self.head:
            return False
        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        return False

    def find_sum(self, data: T) -> int:
        """
        Returns the number of occurrences of `data` in this list
        :param data: data to find and sum up
        :return: number of times the data occurred
        """
        count = 0
        if not self.head:
            return 0
        temp = self.head
        while temp:
            if temp.data == data:
                count += 1
            temp = temp.next
        return count



def help_mario(roster: SLL, ally: str) -> bool:
    """
    Updates the roster of racers to put Mario's ally at the front
    Preserves relative order of racers around ally
    :param roster: initial order of racers
    :param ally: the racer that needs to go first
    :return: True if the roster was changed, else False
    """
    if not roster.head:
        return False
    if roster.head.data == ally:
        return False

    prev, temp = None, roster.head
    while temp:
        if temp.data == ally:
            if temp == roster.tail:
                roster.tail.next = roster.head
                roster.head = temp
                roster.tail = prev
                roster.tail.next = None
                return True
            else:
                roster.tail.next = roster.head
                prev.next = None
                roster.head = temp
                roster.tail = prev
                return True
        prev = temp
        temp = temp.next
    return False
