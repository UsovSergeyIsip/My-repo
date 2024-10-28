# 1.
n =[]
a = input(": ")
b = str(len(a) * 75)
for i in range(len(a)):
    n.append(a[i])
l = 0
p = 0
h = []
for j in range(len(n)):
    l = p
    if n.count(n[j]) > l:
        h.append(n[j])
        p = n.count(n[j])
l = 2
p = 2
g = []
for y in range(len(n)):
    l = p
    if n.count(n[y]) < l:
        g.append(n[y])
        p = n.count(n[y])

m = str(a.count((h[-1])) * 75)
u = str(a.count((g[-1])) * 75)     
print(a,"стоит:",b[:len(b)-2],"рублей",b[-2]+b[-1],"копеек")   
print("Частый символ","'",h[-1],"':",m[:len(m)-2],"рублей",m[-2]+m[-1],"копеек")

print("редкий символ","'",g[0],"':",u[:len(u)-2],"рублей",u[-2]+u[-1],"копеек")