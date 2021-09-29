def merge_sort(arr):
	_len = len(arr)
	if _len == 1:
		return arr
	A = arr[:_len//2] 
	B = arr[_len//2:]
	result_1 = merge_sort(A)
	result_2 = merge_sort(B)
	return merge(result_1, result_2)


def merge(A, B = []):
	response = []
	index_a = 0
	index_b = 0
	len_a = len(A) - 1
	len_b = len(B) - 1

	while index_a <= len_a and index_b <= len_b:
		if A[index_a] < B[index_b]:
			response.append(A[index_a])
			index_a += 1
		else:
			response.append(B[index_b])
			index_b += 1

	if index_a <= len_a:
		response += A[index_a:]
	else: 
		response += B[index_b:]

	return response


def main():
	a = [100, 6, 4 , 9.6 , 29, 5, 34400, -9, -8.6, 4, 0, 1_000_000]
	# Prueba de estabilidad
	a = merge_sort(a)
	print(a)
	a = merge_sort(a)
	print(a)


if __name__ == '__main__':
	main()