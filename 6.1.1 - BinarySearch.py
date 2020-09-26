#В первой строке даны целое число 1≤n≤10^5 
# и массив A[1…n] из n различных натуральных чисел, не превышающих 10^9, 
# в порядке возрастания, во второй — целое число 1≤k≤10^5 
# и k натуральных чисел, не превышающих 10^9.
# Для каждого i от 1 до k необходимо вывести индекс 1≤j≤n, для которого A[j]=bi 
# или -1, если такого j нет.

def DevEtEmp (li, ex):
    i = 0
    j = len(li)-1
    m = int(j/2)
    while li[m] != ex and i < j:
        if ex > li[m]:
            i = m+1
        else:
            j = m-1
        m = int((i+j)/2)
    # если числа нет в массиве
    if i > j:
        return -1
    # если число есть в массиве
    else:
        return m
    

n_array =[] 
n_array = list(map(int, input().split()))
n=n_array.pop(0)
k_array =[]  
k_array = list(map(int, input().split()))
k=k_array.pop(0)
print(n_array)
print(k_array)
count = 0
while count<=k:
    print(DevEtEmp(n_array,k_array(count)))
    count=count+1
