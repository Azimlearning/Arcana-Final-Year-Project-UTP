import json, collections
p=r"C:/Users/User/Documents/FYP DOCS/Arcana-v2/data/eval-live-live/graph.json"
g=json.load(open(p,encoding='utf-8'))
print(type(g), list(g.keys())[:10] if isinstance(g,dict) else len(g))
for k,v in g.items():
    if isinstance(v,list): print(k,len(v), json.dumps(v[0])[:400])
    elif isinstance(v,dict): print(k,'dict',len(v), list(v.items())[:1] and json.dumps(list(v.items())[0])[:400])
    else: print(k,v)
