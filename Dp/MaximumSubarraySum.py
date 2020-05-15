# The task is to find a subarray (contiguous elements) of the given array that has the largest sum.
# Algorithm is also known as Kadane Algorithm
# Python Implementation

def kadane_Algo(A):
	temporary_max = original_max = A[0]
	for x in A[1:]:
		temporary_max = max(x, temporary_max + x)
		original_max = max(original_max, temporary_max)
	return original_max
  
if __name__ == '__main__':
    A = [-1, -3, 4, -1, -2, 1, 5, -3]
    print("Maximum Sum : ", kadane_Algo(A))
