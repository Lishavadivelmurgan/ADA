def subset_sum(arr, target):
    result = []

    def backtrack(index, current_sum, current_subset):
        
        if current_sum == target:
            result.append(current_subset[:])
            return
        
        if current_sum > target or index == len(arr):
            return

       
        current_subset.append(arr[index])
        backtrack(index + 1, current_sum + arr[index], current_subset)

      
        current_subset.pop()

  
        backtrack(index + 1, current_sum, current_subset)

    backtrack(0, 0, [])
    return result



n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements separated by space: ").split()))
target = int(input("Enter target sum: "))

subsets = subset_sum(arr, target)

if subsets:
    print("Subsets with given sum:")
    for s in subsets:
        print(s)
else:
    print("No subset found.")