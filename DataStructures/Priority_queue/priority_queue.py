from DataStructures.Priority_queue import pq_entry as pqe

def default_compare_higher_value(father_node, child_node):
    if pqe.get_priority(father_node) >= pqe.get_priority(child_node):
        return True
    return False

def default_compare_lower_value(father_node, child_node):
    if pqe.get_priority(father_node) <= pqe.get_priority(child_node):
        return True
    return False

def new_heap(is_min_pq):
    cmp=default_compare_lower_value()
    if is_min_pq is False:
        cmp=default_compare_higher_value()
          
    queue={
     'elements': {
         'elements': [],
         'size': 1
     },
         'size': 0,
    'cmp_function': cmp
    }
    return queue