return
        elif root.start_time == start_time:
            return False
        elif root.start_time > start_time:
            if root.left:
                root.left.insert(start_time, end_time, flight_number)
            else:
                root.left = runway_bst(start_time, end_time, flight_number)
                return True
        else:
            if root.right:
                root.right.insert(start_time, end_time, flight_number)
            else:
                root.right = runway_bst(start_time, end_time, flight_number)
                return True
