def init():
    heap = []
    idx_map = {}
    return heap, idx_map


# insert (val, other) into heap
# val must be something that can be compared with '>, ==, <' operators
# other is misc info to save along with, such as idx
# idx must be provided unless idx_map is None
# if idx_map is not None, then idx must be provided
# if idx is already in idx_map, then it will update the value only if val is less than corresponding val in the heap
def insert(heap, val, other=None, idx_map=None, idx=None):
    if idx_map == None and idx != None or idx_map != None and idx == None:
        print "Error! Both idx_map and idx must be None or not None"
        return
    pos = len(heap)
    if idx_map == None:
        # simple heap
        data = (val, other)
        heap += [data]
        up_heapify(heap, pos)
    else:
        data = (val, other, idx)
        if idx not in idx_map:
            # insert new
            idx_map[idx] = pos
            heap += [data]
            up_heapify(heap, pos, idx_map)
        elif val < heap[idx_map[idx]][0]:
            # update the value
            pos = idx_map[idx]
            heap[pos] = data
            up_heapify(heap, pos, idx_map)

            
def up_heapify(heap, pos, idx_map=None):
    if pos == 0:
        return
    parent_pos = parent(pos)
    if heap[pos][0] < heap[parent_pos][0]:
        swap(heap, pos, parent_pos, idx_map)
        up_heapify(heap, parent_pos, idx_map)


def swap(heap, i, j, idx_map):
    if i == j:
        return
    (heap[i], heap[j]) = (heap[j], heap[i])
    if idx_map != None:
        idx_map[heap[i][2]] = i
        idx_map[heap[j][2]] = j


def popmin(heap, idx_map=None):
    pos = len(heap)-1
    swap(heap, 0, pos, idx_map)
    data = heap[pos]
    del heap[pos]
    down_heapify(heap, 0, idx_map)
    return data


def down_heapify(heap, pos, idx_map=None):
    nc = num_children(heap, pos)
    if nc == 0:
        return
    child_pos = left(pos)
    child_val = heap[child_pos][0]
    if nc == 2:
        right_pos = right(pos)
        right_val = heap[right_pos][0]
        if right_val < child_val:
            child_val = right_val
            child_pos = right_pos
    if heap[pos][0] > child_val:
        swap(heap, pos, child_pos, idx_map)
        down_heapify(heap, child_pos, idx_map)
    

def parent(pos):
    return (pos - 1) / 2


def left(pos):
    return pos*2 + 1


def right(pos):
    return pos*2 + 2


def num_children(heap, pos):
    if right(pos) < len(heap):
        return 2
    if left(pos) < len(heap):
        return 1
    return 0


def test1():
    import random
    heap, idx_map = init()
    for _ in range(100):
        insert(heap, random.randint(0, 100))
    while len(heap) > 0:
        print popmin(heap)

def test2():
    import random
    heap, idx_map = init()
    for _ in range(100):
        val = random.randint(0, 100)
        insert(heap, val, val%10)
    while len(heap) > 0:
        print popmin(heap)


def test3():
    import random
    heap, idx_map = init()
    for _ in range(100):
        val = random.randint(0, 100)
        insert(heap, val, str(val), idx_map, val%10)
    while len(heap) > 0:
        print popmin(heap)

