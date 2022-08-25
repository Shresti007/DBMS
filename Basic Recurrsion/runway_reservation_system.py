import datetime

# Datetime python lib useful for this mini project
# https://docs.python.org/3/library/datetime.html

# This class represents a node in the BST.
class runway_bst(object):
    def __init__(root, start_time=None, end_time=None, flight_number=None):
        root.start_time = start_time
        root.end_time = end_time
        root.flight_number = flight_number
        # Left and right child
        root.left = None
        root.right = None
    
    # Implement the insert method in here. 
    # For the node key value comaprision, consider start_time of every node
    # consider the boundary case where root is not available
    # remove pass keyword and implement the method
    
    def insert(root, start_time=None, end_time=None, flight_number=None):
        pass

    # This method validates the interval duration to be 30 mins exact.
	# You need to use datetime strptime to convert string to Date object. 
	# And then perform comparisons on datetime objects.

    def valid_interval(root, start_time, end_time):
		request_start_time = datetime.datetime.strptime(start_time, "%H:%M")
	    request_end_time = datetime.datetime.strptime(end_time, "%H:%M")
  
        tdelta = request_end_time - request_start_time
        if int(tdelta.total_seconds()/60) == 30:
            return True
        else:
            return False
    
    # This method will check if the given time slot is available and no other flight is scheduled
    # remove the pass keyword and implement the logic in this method
	# This method checks if the requested interval overlaps any existing interval. 
	# This returns the list [root.flight_number, root.start_time, root.end_time] of scheduled flight
	# if an overlap is found. Returns None otherwise.
	# You need to use datetime strptime to convert string to Date object. 
	# And then perform comparisons on datetime objects.

    def busy_runway(root, start_time, end_time):
        pass
    
    
    # This method will have logical implementation to make the reservation for a particular flight
    # Before booking the reservation it will validate if the slot is getting booked for 30 minutes only
    # It will also check if the no other flight is scheduled over the runway during that time 
    # remove pass keyword and write the logic
    # Driver method which makes the reservation and calls all the helper methods.
    def make_reservation(root, flight_start_time, flight_end_time, flight_number):
        pass

    def inorder(root, vals):
        if root.left is not None:
            root.left.inorder(vals)
        if root.start_time is not None:
            vals.append(root.start_time)
        if root.right is not None:
            root.right.inorder(vals)
        return vals
        
if __name__ == '__main__':
    
	# Root node of BST
    test = runway_bst('11:00', '11:30', 'GOI9872')
    test.make_reservation('11:35', '12:05', 'JET9874')
    test.make_reservation('12:30', '13:00', 'JET9243')
    
    #Following case should fail. Runway is busy
    test.make_reservation('10:45', '11:15', 'VIS9000')
    test.make_reservation('12:45', '13:15', 'IND3360')
    test.make_reservation('13:45', '14:45', 'IND3361')

    # New booking. Should pass
    test.make_reservation('10:10', '10:40', 'JET9243')
    test.make_reservation('09:30', '10:00', 'AIR2781')

    # verfiying if the data inserted is BST or not 
    res = []
    res = test.inorder(res)
    print(res)
