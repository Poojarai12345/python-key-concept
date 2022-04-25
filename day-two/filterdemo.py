listx=[34,356,3,534,534,342,23,53,5634,634,34,345,343,645]

result=filter(lambda x: True if x%2==0 else False,listx)
print(list(result))

result1=filter(lambda x:True if x>300 else False,listx )
print(list(result1))


#filter also need callback to be passed 
#callback has to return boolean and the callback will be called for each 
#each element in the collection if the callback return true the element 
#would be kept in tact otherwise filter will be called 
# in the result only filter element II be presenet 
# if the input list has n element output list will have <=n element 
