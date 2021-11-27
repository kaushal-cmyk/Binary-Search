
###--------------- Binary Search Algorithm -----------### 

####----------searching function -----------####
def search(a, n):
    
    l = 0
    u = len(a) - 1
    
    while(l <= u):
        mid = (l + u) // 2 
        
        if(a[mid] == n ):
            globals() ['pos'] = mid
            return True
        else:
            if(a[mid] < n):
                l = mid + 1
            else:
                u = mid - 1
    return False



a = []
b = int(input("enter the total no of elements in the list:"))
for i in range(1, b + 1) :
    c = int(input("enter the elements in the list:"))
    a.append(c)
n = int(input("enter the number to search in the list:"))

a.sort()
print("the entered list is ",a)
pos = -1

if search(a, n):
    print("th number " , n, " found at :",pos + 1," index")
else:
    print("not found")


k=input("press enter to exit") 