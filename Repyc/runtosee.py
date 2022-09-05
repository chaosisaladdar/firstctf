
a = 0
b = ~a * ~a #b=1
c = b + b   #c=2

t = a
t2 = a
m = [a] * c ** (c * c)
key1 = [a] * 100
key2 = []
print(m)
print(len(m))
print(key1)
x = [
 [#m[0]=="Authentication token: "
  'mov2', a, 'Authentication token: '],
 [#key1[0]=="答案"
  'input2', a, a],
 [#m[6]=="á×äÓâæíäàßåÉÛãåäÉÖÓÉäà......."
  'mov2', 6, 'á×äÓâæíäàßåÉÛãåäÉÖÓÉäàÓÉÖÓåäÉÓÚÕæïèäßÙÚÉÛÓäàÙÔÉÓâæÉàÓÚÕÓÒÙæäàÉäàßåÉßåÉäàÓÉÚÓáÉ·Ôâ×ÚÕÓÔÉ³ÚÕæïèäßÙÚÉÅä×ÚÔ×æÔÉ×Úïá×ïåÉßÉÔÙÚäÉæÓ×ÜÜïÉà×âÓÉ×ÉÑÙÙÔÉâßÔÉÖãäÉßÉæÓ×ÜÜïÉÓÚÞÙïÉäàßåÉåÙÚÑÉßÉàÙèÓÉïÙãÉáßÜÜÉÓÚÞÙïÉßäÉ×åáÓÜÜ\x97ÉïÙãäãÖÓ\x9aÕÙÛ\x99á×äÕà©â«³£ï²ÕÔÈ·±â¨ë'],
 [#m[2]==2**(3*2+1)-2**(2+1)==120
  'mov2', c, c ** (3 * c + b) - c ** (c + b)],
 [#m[4]==15
  'mov2', 4, 15],
 [#m[3]==1
  'mov2', 3, b],
 [#m[2]==m[2]*m[3]==120
  'X', c, c, 3],
 [#m[2]==m[2]+m[4]==135
  'ADD', c, c, 4],
 [#m[0]==m[0]
  'mov', a, c],
 [#m[3]==0
  'mov5', 3],
 [#m[6]==m[6]^m[3]
  'for XOR', 6, 3],
 [#m[0]=="Thanks."
  'mov2', a, 'Thanks.'],
 [#m[1]=="Authorizing access..."
  'mov2', b, 'Authorizing access...'],
 [#print("Thanks.")
  'print1', a],
 [#m[0]==key1[0]
  'mov4', a, a],
 [#m[0]==m[0]^m[2]
  'for XOR', a, c],
 [#m[0]==m[0]-m[4]
  'for SUB', a, 4],
 [#m[5]==19
  'mov2', 5, 19],
 [#m[0]!=a[6]
  'cmp', a, 6, 5],
 [#print("Authorizing access...")
  'print1', b],
 [
  'NULL'],
 [#m[1]=="Access denied!"
  'mov2', b, 'Access denied!'],
 [#print("Access denied!")
  'print1', b],
 [
  'NULL']]

x1 = x[t][a].lower()
x2 = x[t][b:]
print(x1)
print(x2)
print(a)
print(b)