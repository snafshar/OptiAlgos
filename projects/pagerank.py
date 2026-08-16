def rank(edges,d=.85):
 nodes=sorted(set(edges)|{v for vs in edges.values() for v in vs});n=len(nodes);r={v:1/n for v in nodes}
 for _ in range(100):
  new={v:(1-d)/n for v in nodes}
  for u,score in r.items():
   for v in edges.get(u,[]):new[v]+=d*score/len(edges[u])
  r=new
 return r
if __name__=='__main__':print(rank({'a':['b'],'b':['a']}))