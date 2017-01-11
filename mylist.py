#!/usr/bin/python3

class LinkedListItem:
    def __init__(self, actual_data, next_item = None):
        self.actual_data = actual_data
        self.next_item = next_item

    def __str__(self):
        return "{0}".format(str(self.actual_data))


class MyList:
    """
    List implementation

    Attributes:
    length(int) : The number of elements in the list
    first_item(LinkedListitem) : the first item of the list
    """
    def __init__(self, alist = None):

        self.length = 0
        self.first_item = None
        if alist:
            for item in alist:
                self.append(item)

    def __str__(self):
        """
        """
        ret = '['
        item = self.first_item
        while item:
            if isinstance(item.actual_data, str, int, float)):
                ret  += "'{0}'".format(item)
            else: # types such as list or tuple or objects don't have quotes
                ret  += "{0}".format(item)
            item = item.next_item
            if item:
                ret += ", "
        ret += ']'

        return ret

    def index(self, obj):
        """The method index() returns the lowest index in list that obj appears.
        Args:
            obj (obj): The obj to be found.

        Returns:
            int: The lowest index number in list that obj appears.

        Raises:
           ValueError: Indicating the value is not be found.

        """
        i = 0
        item = self.first_item
        while item:
            if obj == item.actual_data:
                return i
            item = item.next_item
            i += 1
        raise ValueError("'{0}' is not  in list".format(obj))

    def count(self, obj):
        """ This method returns count of how many times obj occurs in list. """
        cpt = 0
        item = self.first_item
        while item:
            if obj == item.actual_data:
                cpt += 1
            item = item.next_item

        return cpt

    def is_present(self, obj):
        """ This method retuns True if obj is present in the list, False otherwise."""
        item = self.first_item
        while item:
            if obj == item.actual_data:
                return True
            item = item.next_item

        return False

    def append(self, actual_data):
        """ Add an item to the list. """
        if not self.first_item:
            self.first_item = LinkedListItem(actual_data)
        else:
            item = self.first_item
            while item.next_item:
                item = item.next_item
            item.next_item = LinkedListItem(actual_data)
        self.length += 1

    # def extend(self):
    #     """
    #     """
    #     pass

    # def insert(index, element):
    #     """
    #     """
    #     pass

    # def delete(index):
    #     """
    #     """
    #     pass

    # def remove(element):
    #     """
    #     """
    #     pass

    # def pop(element):
    #     """
    #     """
    #     pass

    # def slice(pattern):
    #     """
    #     """
    #     pass

    # def is_true():
    #     """
    #     """
    #     pass

    # def sort():
    #     """
    #     """
    #     pass

    # def reverse():
    #     """
    #     """
    #     pass
    # def copy():
    #     """"
    #     """
    #     pass

    def clear(self):
        """ Reset the list. """
        self.length = 0
        self.first_item = None

é"é"é"é"é"é"éé"é"é"é"é"é""'"'"'"'"'"''"'"'"'é"é"é"é"é"é"23232332é"é"é"é"
