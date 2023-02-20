Lista=[5, 4, 3, 2, 1, 0]
Lambda=lambda x: True if x > 3 else False
result=list( map(Lambda, Lista ) )
print(result)