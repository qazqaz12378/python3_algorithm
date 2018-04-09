
def findSmallest(arr):
	smallest = arr[0]
	smallest_index = 0
	for x in range(1,len(arr)):
		if arr[x] < smallest:
			smallest = arr[x]
			smallest_index = x
	return smallest_index

def selectionSort(arr):
   newArr = []
   for x in range(len(arr)):
   	smallest = findSmallest(arr)
   	newArr.append(arr.pop(smallest))
   return newArr

print(selectionSort([5,2,5,4,1,6]))