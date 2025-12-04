import heapq

h = []
heapq.heappush(h,10)
heapq.heappush(h,40)
heapq.heappush(h,5)
print(h)
heapq.heappop(h) #returns min value and remove from heap
print(h)

g = [20,40,55,22]
heapq.heapify(g)
print(g)
heapq.heapify_max(g)#transforms list to max heap added in 3.14
print(g)

heapq.heappushpop(h,66) #pushes 66 and returns smallest value and deletes it #here 66 adds and 10 dele
print(h)
heapq.heapreplace(h,75) #removes min element and adds 75
print(h)

heap = [1,20,5,4,3,6,2]
print(heapq.nsmallest(2,heap)) #gives first 2 smallest numbers
print(heapq.nlargest(3,heap)) #gives first 3 largest numbers

list1 = [(1,'ria'), (4,'sia'), (3,'gia')]
heapq.heapify(list1)
print(list1)
for i in range(len(list1)):
    print(heapq.heappop(list1)) #1 ria is highest priority so it gets removed first
