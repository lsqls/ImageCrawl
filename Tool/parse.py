import  os
import sys
import  ast
with  open('data.json','r') as f:
    data=f.read()
info=ast.literal_eval(data)
with  open('tiebalist.txt','w') as f:
    for  i  in info:
        f.write(i['url']+'\n')
