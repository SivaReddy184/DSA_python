table_size = 7
hash_table = [None]*table_size
DELETED = object()
print(hash_table)

def hashing(key):
    return hash(key) % table_size

def insert(key, value):
    index = hashing(key)
    original_index = index
    while hash_table[index] is not None and hash_table[index] is not DELETED:
        if hash_table[index][0] == key:
            hash_table[index][1] = value
            return
        index = (index+1) % table_size
        if index == original_index:
            print('Hashtable is Full')
            return
    hash_table[index] = (key, value)
def search(key):
    index = hashing(key)
    original_index = index
    while hash_table[index] is not None:
        if hash_table[index] is not DELETED and hash_table[index][0] == key:
            return hash_table[index][1]
        index = (index+1) % table_size
        if index == original_index:
            break
    return None

def delete(key):
    index = hashing(key)
    original_index = index
    while hash_table[index] is not None:
        if hash_table[index] is not DELETED and hash_table[index][0] == key:
            hash_table[index] = DELETED
            return True
        index = (index+1) % table_size
        if index == original_index:
            break
    return False


def display():
    for i, item in enumerate(hash_table):
        if item is DELETED:
            print('index', i, ':', 'DELETED')
        else:
            print('index', i, ':', item)

print('begin')
display()
print('----------')

insert('a', 'apple')
insert('b', 'bat')
insert('c', 'cat')
print('after insertion')
display()
print('------------')
print(search('a'))
print('after deletion')
delete('a')
display()
