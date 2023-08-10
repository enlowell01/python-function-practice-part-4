def max_num(x, y, z):
    return max([x,y,z])

def mult_list(nums):
    if len(nums) == 0:
        return 0
    product = nums[0]
    if len(nums) > 1:
        for num in nums[1:]:
            product = product * num
    return product

def rev_string(str):
    return str[::-1]

def num_within(x, start, end):
    return x in range(start, end + 1)

triangle = [[1], [1,1]]
def pascal(n):
    if n < 1:
        print('not enough rows')
    elif n == 1:
        print(triangle[0])
    else:
        row_num = 2
        while len(triangle) < n:
            row = []
            row_before = triangle[row_num - 1]
            length = len(row_before) + 1
            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i > 0 and  i < (length - 1):
                    row.append(triangle[row_num - 1][i - 1] + triangle[row_num - 1][i])
                else:
                    row.append(1)
            triangle.append(row)
            row_num += 1
        for row in triangle:
            print(row)


