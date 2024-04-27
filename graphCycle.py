d={0:[1,4],1:[2],2:[3],3:[1],4:[3],5:[0]}
source=int(input("enter source:"))
destination=int(input("enter destination:"))
v=set()
def dfs(source,v):
    v.add(source)
    if source==destination:
        print(source,"is in cycle")
        return True         
    for i in d[source]:
        if i not in v:
            if dfs(i,v):
                return True 
    return False
dfs(source,v)
