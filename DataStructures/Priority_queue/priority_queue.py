from DataStructures.List import array_list as lt
from DataStructures.Priority_queue import pq_entry as pqe

def default_compare_higher_value(father_node, child_node):
    if pqe.get_priority(father_node) >= pqe.get_priority(child_node):
        return True
    return False

def default_compare_lower_value(father_node, child_node):
    if pqe.get_priority(father_node) <= pqe.get_priority(child_node):
        return True
    return False

def is_empty(my_heap):
    return size(my_heap) == 0

def new_heap(is_min_pq=True):
    heap = {
        'elements': lt.new_list('ARRAY_LIST'),
        'size': 0,
        'cmp_function': None
    }
    if is_min_pq:
        heap['cmp_function'] = default_compare_lower_value
    else:
        heap['cmp_function'] = default_compare_higher_value

    lt.add_last(heap['elements'], None)

    return heap

def exchange(my_heap, pos1, pos2):
    elements = my_heap['elements']
    e1 = lt.get_element(elements, pos1)
    e2 = lt.get_element(elements, pos2)
    lt.change_info(elements, pos1, e2)
    lt.change_info(elements, pos2, e1)

def swim(my_heap, pos):
    elements = my_heap['elements']

    while pos > 1:
        parent = pos // 2
        current = lt.get_element(elements, pos)
        father = lt.get_element(elements, parent)

        if not priority(my_heap, father, current):
            exchange(my_heap, pos, parent)
            pos = parent 
        else:
            pos = 1 

def remove(my_heap):
    if is_empty(my_heap):
        return None

    elements = my_heap['elements']
    top = lt.get_element(elements, 1)
    exchange(my_heap, 1, my_heap['size'])
    lt.remove_last(elements)
    my_heap['size'] -= 1
    if my_heap['size'] > 0:
        sink(my_heap, 1)
    return pqe.get_value(top)

def contains(my_heap, value):
    return is_present_value(my_heap, value) != -1


