"""
Session 14A: Stacks and Queues with pancakes
"""

#TODO: Make a plate class that has a color
class Plate:
    pass


#TODO: Make a pancake class that has toppings and acts as a node
class Pancake:
    pass

#TODO: Make a node class that holds a pancake or a plate
class Node:
    __slots__ = ["__value__", "__next__"]
    
    def __init__(self, value, next = None):
        """
        The first node should have the beginning value and next set to None.
        """
        self.__value__ = value
        self.__next__ = next

    def next(self):
        """
        Returns the next node in the sequence
        """
        return self.__next__

    def value(self):
        """
        Returns the current value
        """
        return self.__value__

    def print_node(self, node_seq):
        """
        Prints the nodes in a sequence
        """
        values = list()

        # add the elements onto the list until there are no more next nodes
        while(node_seq.next() != None):
            values.append(node_seq.value())
            node_seq = node_seq.next()

        # add the final element
        values.append(node_seq.value())

        # print the node as a list
        print(values)

#TODO: Make a class for a stack for pancakes. The first value should always be a plate. You should be able to pop, push, and peek
class Stack:
    __slots__ = ["__size__", "__head__", "__next__"]
    
    def __init__(self, head):
        """
        Initialize a stack with no next, a passed in head, and a size of 1
        """
        self.__next__ = None
        self.__head__ = head
        self.__size__ = 1

    def is_empty(self):
        """
        Returns true if empty; false otherwise
        """
        return self.__size__ == 0

    def size(self):
        """
        Returns the size of the stack
        """
        return self.__size__

    def __repr__(self):
        values = []
        current = self.__head__
        while(current != None):
            values.append(self.__head__.value())
            current = current.next()

        return values

    def push(self, value):
        """
        Adds a node with value to the stack
        """
        # set next to the old head
        self.__next__ = self.__head__
        # set the new head to a new node with the old head as next and the passed in value
        self.__head__ = Node(value, self.__next__)

    def peek(self):
        """
        Returns the top value of the stack
        """
        return self.__head__.value()

    def pop(self):
        """
        Return the top value then remove that node from the stack.
        """
        # keep track of the old head
        old_head = self.__head__
        # set the new head to the old next.
        self.__head__ = self.__next__
        # return the previous head
        return old_head


#TODO: Make a queue class for plates. When a pancake stack is create, pop a plate from the queue. When a pancake stack has no more pancakes, push the plate back onto the queue.
class Queue:
    pass

def main():
    n1 = Node(1)
    n2 = Node(2, n1)
    n3 = Node(3, n2)
    n4 = Node(4, n3)

    n4.print_node(n4)
    #TODO: Make 3 plates and add them to a queue.
    #TODO: Create five pancakes
    #TODO: Add the pancakes to a stack of pancakes. Make sure to add a plate first
    #TODO: Peek to see what the top pancake's toppings are
    #TODO: Eat the top pancake by popping from the pancake stack
    #TODO: Add two more pancakes to the stack.
    #TODO: Pop all the pancakes until you only have a plate. Add the plate to the queue
    pass

if __name__ == "__main__":
    main()