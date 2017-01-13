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

        self._length = 0
        self.first_item = None
        if alist:
            self.extend(alist)

    def __str__(self):
        """Human readable representation of the values contained in the list."""
        ret = '['
        item = self.first_item
        while item:
            if isinstance(item.actual_data, (str, int, float)):
                ret  += "'{0}'".format(item)
            else: # types such as list or tuple or objects don't have quotes
                ret  += "{0}".format(item)
            item = item.next_item
            if item:
                ret += ", "
        ret += ']'

        return ret

    def __increment_length__(self):
        self._length += 1

    def __decrement_length__(self):
        if self._length > 0:
            self._length -= 1

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

    def is_in(self, obj):
        """ This method retuns True if obj is present in the list, False otherwise."""
        item = self.first_item
        while item:
            if obj == item.actual_data:
                return True
            item = item.next_item

        return False

    def append(self, actual_data):
        """ Add an item to the list.

        Return Value:
        This method does not return any value but add the content to the existing list.
        """
        if not self.first_item:
            self.first_item = LinkedListItem(actual_data)
        else:
            item = self.first_item
            while item.next_item:
                item = item.next_item
            item.next_item = LinkedListItem(actual_data)
        self.__increment_length__()

    def extend(self, seq):
         """This method appends the contents of seq to the list.

         Return Value:
         This method does not return any value but add the content to the existing list.
         """
         for item in seq:
                self.append(item)



    def insert(self, index, obj):
        """The method insert() inserts object obj into list at offset index.

        Args:
        index (int)
        obj (obj)

        Return Value:
        The method insert() does not return any value but insert an element at the given index.
        """

        if index > self._length:
            index = self._length

        prev = None
        cur = self.first_item
        i = 0
        while i < index:
            prev = cur
            cur = cur.next_item
            i += 1
        if prev:
            prev.next_item = LinkedListItem(obj, cur)
        else:
            self.first_item = LinkedListItem(obj, cur)
        self.__increment_length__()

    # def delete(index):
    #     """
    #     """
    #     pass

    def remove(self, obj):
        """
        Remove the first item from the list whose value is obj.

        Args:
        obj (obj): The object to be found

        Return value:
        None

        Raises:
        ValueError : It is an error if there is no such item.
        """
        previous_item = None
        current_item = self.first_item
        while current_item:
            if current_item.actual_data == obj:
                if previous_item:
                    previous_item.next_item = current_item.next_item
                else:
                    self.first_item = current_item.next_item
                self.__decrement_length__()
                return None
            previous_item = current_item
            current_item = current_item.next_item
        else:
            raise ValueError("list.remove(x): x not in list")

    def pop(obj):
        """
        """
        pass

    # def slice(pattern):
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
        self._length = 0
        self.first_item = None

