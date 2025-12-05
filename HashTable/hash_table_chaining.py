table_size = 10

hash_table = [ [] for _ in range(table_size)]

def hashing(key):
    return hash(key) % table_size

def insert(key, value):
    index = hashing(key)
    #print(hash(key))
    for item in hash_table[index]:
        if item[0] == key:
            item[1] = value
            return
    hash_table[index].append([key, value])

def search(key):
    index = hashing(key)
    for item in hash_table[index]:
        if item[0] == key:
            return item[1]
    return None

def delete(key):
    index = hashing(key)
    # for i in hash_table[index]:
    #     if i[0] == key:
    #         hash_table[index].remove(i)
    #         return
    for i,item in enumerate(hash_table[index]):
        if item[0] == key:
            del hash_table[index][i]
            return

def display():
    for i, item in enumerate(hash_table):
        print('bucket', i, ':', item)

display()
insert('a', 'apple')
insert('b', 'bat')
insert('c', 'cat')
print('after insertion: ')
delete('a')
display()
print(search('b'))
