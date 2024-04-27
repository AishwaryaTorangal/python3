d={0:[1,4],1:[2],2:[3],3:[1],4:[3],5:[0]}
v=set()
 def dfs(source,v):
    v.add(source)
    if source==destination:
        return True 
    for i in d[source]:
        if i not in v:
            if dfs(i,v):
                return True   
    return False
 return dfs(source,v)
