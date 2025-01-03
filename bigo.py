#O(1) かならず先頭のデータを渡す
def func1(numbers):
    return numbers[0]

#O(log₂(n))
def func2(n):
    if n<= 1:
        return
    else:
        print(n)
        func2(n/2)


# O(n)
def func3(numbers):
    for number in numbers:
        print(number)

#O(n * logn(n))
def func4(numbers):
    for i in range(int(n)):
        print(i, end=" ")
    print()

# O(n²)
def func5(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            print(i,j)
        print()



if __name__ == "__main__":
    #result1 = func1([1,2,3])
    #print(result1)
    #func2(10)
    func5([1,2,3,4])



    