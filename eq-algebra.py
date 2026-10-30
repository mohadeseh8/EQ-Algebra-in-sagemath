# ==========================================
# Finite EQ-Algebra Implementation
# Based on Example 1
# ==========================================

# Set of elements
L = ['0', 'a', 'b', '1']

# Meet operation
meet = {
('0','0'):'0', ('0','a'):'0', ('0','b'):'0', ('0','1'):'0',
('a','0'):'0', ('a','a'):'a', ('a','b'):'a', ('a','1'):'a',
('b','0'):'0', ('b','a'):'a', ('b','b'):'b', ('b','1'):'b',
('1','0'):'0', ('1','a'):'a', ('1','b'):'b', ('1','1'):'1'
}

# Product operation
product = meet.copy()

# Equality operation
eq = {
('0','0'):'1', ('0','a'):'0', ('0','b'):'0', ('0','1'):'0',
('a','0'):'0', ('a','a'):'1', ('a','b'):'a', ('a','1'):'a',
('b','0'):'0', ('b','a'):'a', ('b','b'):'1', ('b','1'):'1',
('1','0'):'0', ('1','a'):'a', ('1','b'):'1', ('1','1'):'1'
}

# Order relation
def leq(x,y):
    return meet[(x,y)] == x

# Implication operation
def implication(x,y):
    return eq[(meet[(x,y)],x)]

# ==========================================
# Verification of EQ-algebra axioms
# ==========================================

E1 = all(
    meet[(meet[(x,y)],z)] == meet[(x,meet[(y,z)])]
    and meet[(x,y)] == meet[(y,x)]
    and meet[(x,x)] == x
    and meet[(x,'1')] == x
    for x in L for y in L for z in L
)

E2 = all(
    product[(product[(x,y)],z)]
    == product[(x,product[(y,z)])]
    and product[(x,'1')] == x
    and (
        not leq(x,y)
        or leq(product[(x,z)],product[(y,z)])
    )
    for x in L for y in L for z in L
)

E3 = all(eq[(x,x)] == '1' for x in L)

E4 = all(
    leq(
        product[(eq[(meet[(a,b)],c)],eq[(d,a)])],
        eq[(c,meet[(d,b)])]
    )
    for a in L for b in L for c in L for d in L
)

E5 = all(
    leq(
        product[(eq[(a,b)],eq[(c,d)])],
        eq[(eq[(a,c)],eq[(b,d)])]
    )
    for a in L for b in L for c in L for d in L
)

E6 = all(
    leq(
        eq[(meet[(meet[(a,b)],c)],a)],
        eq[(meet[(a,b)],a)]
    )
    for a in L for b in L for c in L
)

E7 = all(
    leq(product[(a,b)],eq[(a,b)])
    for a in L for b in L
)

print("E1:", E1)
print("E2:", E2)
print("E3:", E3)
print("E4:", E4)
print("E5:", E5)
print("E6:", E6)
print("E7:", E7)

print("----------------------")

print("Is EQ-algebra:",
      all([E1,E2,E3,E4,E5,E6,E7]))

# ==========================================
# Integral Prefilter verification
# ==========================================

F = {'1','b'}

# Prefilter conditions
F1 = '1' in F

F2 = all(
    not (x in F and implication(x,y) in F)
    or y in F
    for x in L for y in L
)

# Negation
def neg(x):
    return eq[(x,'0')]

# Integral prefilter condition
IP = all(
    not (neg(product[(x,y)]) in F)
    or neg(x) in F
    or neg(y) in F
    for x in L for y in L
)

print("Prefilter:", F1 and F2)
print("Integral Prefilter:", IP)
