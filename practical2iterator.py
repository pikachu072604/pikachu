print("----ITERATABLES-----")
lst1=["mumbai","pune","delhi","patna"]
for city in lst1:
    print(city)
print("\n")
print("----Iterators-----")
iterator_obj=iter(lst1)
try:
    print(next(iterator_obj))
    print(next(iterator_obj))
    print(next(iterator_obj))
    print(next(iterator_obj))
    print(next(iterator_obj))
except:
    print("Stop Iteration Exception Raised")
    
