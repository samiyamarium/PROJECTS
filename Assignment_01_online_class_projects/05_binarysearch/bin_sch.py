def bin_sch(l,target,low=None,high=None):
    
    if low is None:
        low=0
    if high is None:
            high=len(l)-1
    if high<low:
            return "Wrong Target  ",-1 #target not available
    midpoint=(low+high)//2
    if l[midpoint] == target:
            return "You found at index",midpoint
    elif target<l[midpoint]:
            return bin_sch(l,target,low,midpoint-1)
    else:
             return bin_sch(l,target,midpoint+1,high)

#l=[1,2,3,4,5]
#target=10  #returned -1 since target is not in  list
l = [1, 2, 3, 4, 5]
target = 3 # output: found at position 3
l = [1, 2, 3, 4, 5, 7 ,11]
target = 11 # output: found at position 6

print(bin_sch(l,target))