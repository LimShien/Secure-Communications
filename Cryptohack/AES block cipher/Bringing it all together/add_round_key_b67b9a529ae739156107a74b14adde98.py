state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    l1 =[]
    l2 =[]

    for x in s:
        for y in x:
            l1.append(y)
    for i in k:
        for j in i:
            l2.append(j)
    
    count=0
    l3 =[]
    while count<len(l1):
        l3.append(l1[count] ^ l2[count])

        count+=1

    
    return l3

def matrix2bytes(matrix):
   """ Converts a 4x4 matrix into a 16-byte array.  """
   result = ""
   for x in matrix:
        result += chr(x)    
   return result 

print(matrix2bytes(add_round_key(state, round_key)))

