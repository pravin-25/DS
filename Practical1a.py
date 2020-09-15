arr = [45,3,73,9,23,10,35,22]

def linear_search(arr,n):
	for i in range(len(arr)):
		if arr[i] == n:
			return i
	return -1
	
print(linear_search(arr,9))

def bubble_sort(arr):
	len_arr=len(arr)
	for i in range(len_arr):
		for j in range(0, len_arr-i-1):
			if arr[j] > arr[j+1]:
				arr[j],arr[j+1] = arr[j+1],arr[j]
	return arr

print(bubble_sort(arr))

def merge_arr(arr,element):
	new_arr =arr.append(element)
	return arr
print(merge_arr(arr,14))

def reverse(arr):
	new_arr=arr.reverse()
	return arr
print (reverse(arr))
