def count_unique_element(input_list):    
    unique=set(input_list)
    output=len(unique)
    print(output)

set1=set(map(int, input().split()))
count_unique_element(set1)