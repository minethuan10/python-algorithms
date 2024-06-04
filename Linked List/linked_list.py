#Example for the Node class

#The Node Class
class Node(object):
    def __init__(self,val):
        self.val=val
        self.next=None
    def get_data(self):
        return self.val
    def set_data(self,val):
        self.val=val
    def get_next(self):
        return self.next
    def self_next(self, nxt):
        self.next=nxt