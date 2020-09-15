X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

def addition(X,Y):
	print("Addition")
	for i in range(len(X)):
		for j in range(len(X[0])):
			result[i][j] = X[i][j] + Y[i][j]

	for r in result:
		print(r)
		
addition(X,Y)

def multiplication(X,Y):
	print("Multiplication ")
	for i in range(len(X)):
		for j in range(len(Y[0])):
			for k in range(len(Y)):
				result[i][j] += X[i][k] * Y[k][j]

	for r in result:
		print(r)

multiplication(X,Y)

def transpose(X):
	for i in range(len(X)):
		for j in range(len(X[0])):
			result[j][i] = X[i][j]

	for r in result:
		print(r)

print("Transpose of X")
transpose(X)
print("Transpose of Y")
transpose(Y)