# custom list

class CustomList:
    # initialize an empty list
    def __init__(self):
        self.list = []

    # a function to add elements to the list
    def add(self,value):
        self.list.append(value)

    # a function to remove elements
    def remove(self,value):
        if value in self.list:
            self.list.remove(value)
        else:
            print("There are no value in the list")

    # a function to get an element from the list
    def get(self,index):
        if 0<= index <= len(self.list):
            return self.list[index]
        else:
            print("No element found")

    # a function to return the size of a list
    def size(self):
        return len(self.list)

    # a function to display the list
    def display(self):
        return self.list

list = CustomList()

list.add(1)
list.add(2)
list.add(3)
list.add(4)
list.add(5)


list.remove(1)
list.remove(2)

print("Element at index 2 is ", list.get(2))
print("the size of the list is ", list.size())