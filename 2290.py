import sys
input = sys.stdin.readline
s,n = input().split()
s=int(s)
# print(n,s)
#       --   --        --   --   --   --   --   --  
#    |    |    | |  | |    |       | |  | |  | |  | 
#    |    |    | |  | |    |       | |  | |  | |  | 
#       --   --   --   --   --        --   --       
#    | |       |    |    | |  |    | |  |    | |  | 
#    | |       |    |    | |  |    | |  |    | |  | 
#       --   --        --   --        --   --   --  
top = {1:" "+s*" "+" ",2:" "+s*"-"+" ",3:" "+s*"-"+" ",4:" "+s*" "+" ",5:" "+s*"-"+" ",6:" "+s*"-"+" ",7:" "+s*"-"+" ",8:" "+s*"-"+" ",9:" "+s*"-"+" ",0:" "+s*"-"+" "}
down = {1:" "+s*" "+" ",2:" "+s*"-"+" ",3:" "+s*"-"+" ",4:" "+s*" "+" ",5:" "+s*"-"+" ",6:" "+s*"-"+" ",7:" "+s*" "+" ",8:" "+s*"-"+" ",9:" "+s*"-"+" ",0:" "+s*"-"+" "}
mid = {1:" "+s*" "+" ",2:" "+s*"-"+" ",3:" "+s*"-"+" ",4:" "+s*"-"+" ",5:" "+s*"-"+" ",6:" "+s*"-"+" ",7:" "+s*" "+" ",8:" "+s*"-"+" ",9:" "+s*"-"+" ",0:" "+s*" "+" "}
mid_top = {1:" "+s*" "+"|",2:" "+s*" "+"|",3:" "+s*" "+"|",4:"|"+s*" "+"|",5:"|"+s*" "+" ",6:"|"+s*" "+" ",7:" "+s*" "+"|",8:"|"+s*" "+"|",9:"|"+s*" "+"|",0:"|"+s*" "+"|"}
mid_down = {1:" "+s*" "+"|",2:"|"+s*" "+" ",3:" "+s*" "+"|",4:" "+s*" "+"|",5:" "+s*" "+"|",6:"|"+s*" "+"|",7:" "+s*" "+"|",8:"|"+s*" "+"|",9:" "+s*" "+"|",0:"|"+s*" "+"|"}

for i in range(len(n)):
    print(top[int(n[i])],end=" ")
print()
for i in range(s):
    for d in range(len(n)):
        print(mid_top[int(n[d])],end=" ")
    print()
for i in range(len(n)):
    print(mid[int(n[i])],end=" ")
print()
for i in range(s):
    for d in range(len(n)):
        print(mid_down[int(n[d])],end=" ")
    print()
for i in range(len(n)):
    print(down[int(n[i])],end=" ")
print()

