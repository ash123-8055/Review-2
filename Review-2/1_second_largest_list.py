# Input: [2,11,15,66,20] 
# Output: Second largest: 20


def max_calc(num_list):
    """
    Description: Gives the maximum number in the list
    Parameter: num_list: List containing numbers
    return: Return the max Value
    """
    
    max=0
    for i in num_list:
        i=int(i)
        if i>max:
            max=i
            
    return max

num_list_str=list(input("Enter the list: ").split(","))
num_list=[int(i) for i in num_list_str]
print(num_list)
max=max_calc(num_list)
num_list=[i for i in num_list if i is not max]
max=max_calc(num_list)

print(f"Second largest: {max}")