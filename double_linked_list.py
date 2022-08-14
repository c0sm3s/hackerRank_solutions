from os import remove


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        print("Double-linked list printed forward")
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            
            count+=1
            
            itr = itr.next
        return count

    def insert_at_begining(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next
            

        itr.next = Node(data, None, itr)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        """
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                itr.next.prev = node
                itr.next = node

                break

            itr = itr.next
            count += 1
        """
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1
    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            print(self.get_length())
            raise Exception("Invalid Index")

        if index==0:
            self.head.next.prev = None
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        
        while itr:
            if count == index :
                if itr.next:
                    itr.next.prev = itr.prev
                    itr.prev.next = itr.next
                else:
                    itr.prev.next = None
                
                break

            itr = itr.next
            count+=1
        """
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break

            itr = itr.next
            count+=1
        """

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node
        if self.head is None:
            print("Linked list is empty")
            return
        added = False
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next, itr)
                itr.next.prev = node
                itr.next = node
               

                added = True
                break
            itr = itr.next
            
        if not added:
            print("Value was not found!")
          
    def remove_by_value(self, data):
        # Remove first node that contains data
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        deleted = False
        if self.head.data == data:
            self.head.next.prev = None
            self.head = self.head.next

            return
               
        while itr.next:        
            if itr.next.data == data:
                itr.next.next.prev = itr
                itr.next = itr.next.next
                
                deleted = True
                break
            itr = itr.next
        if not deleted:
            print(data + " was not found! -> remove_by_value")
    
    def print_backward(self):
        # Print linked list in reverse direction. Use node.prev for this.
        print("Double-linked list printed backward")
        if self.head is None:
            print("Linked list is empty")
            return
        ll_len = self.get_length()

        itr = self.head
        llstr = ''
        while itr.next:
            itr = itr.next
            
        while itr:
            # print(itr)
            llstr += str(itr.data)+' --> ' if itr.prev else str(itr.data)
            itr = itr.prev
           
        print(llstr) 

if __name__ == '__main__':
    ll = LinkedList()
    print(ll.get_length())

    ll.insert_at_begining("test05")
    ll.insert_at_begining("test95")
    ll.insert_at_end("test86")
    print('\ninsert_at_begining')
    ll.print_forward()
    ll.print_backward()

    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
        
    ll.insert_at_end("test06")
    print('\n')
    ll.print_forward()
    ll.print_backward()

    ll.insert_after_value("banana","apple") # insert apple after mango
    print('\n')
    ll.print_forward()
    ll.print_backward()

    ll.insert_at(6,"test_00")
    print('\ninsert_at')
    ll.print_forward()
    ll.print_backward()

    ll.insert_at_begining("test05")
    print('\ninsert_at_begining')
    ll.print_forward()
    ll.print_backward()
    
    # ll.remove_at(4)
    print(ll.get_length())
    ll.remove_at(ll.get_length()-1)
    print('\nremove_at')
    ll.print_forward()
    ll.print_backward()

    ll.remove_by_value("test05")
    print('\nremove_by_value')
    ll.print_forward()
    ll.print_backward()

    ll.remove_by_value
    # ll.print_forward()
    # ll.remove_by_value("orange") # remove orange from linked list
    # ll.remove_by_value("banana")
    # ll.print_forward()
    # ll.remove_by_value("figs")
    # ll.print_forward()
    # ll.insert_at_end("test")
    # ll.print_forward()
    # ll.insert_at_end("test02")
    # ll.print_forward()
    # ll.insert_at(2, "test03")
    # ll.print_forward()
    # ll.remove_by_value("mango")
    # ll.remove_by_value("apple")
    # ll.print_forward()
    # ll.remove_by_value("grapes")
   
    
