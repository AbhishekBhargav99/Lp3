def func_permutation(s,t):
	answer =[]
	for i in t:
		answer.append(s[i-1])
	return answer

def func_encryption(txt, key, f):

	ep=[4,1,2,3,2,3,4,1]
	p4=[2,4,3,1]

	lt=txt[:4].copy()
	rt=txt[4:].copy()
	print("Left and Right part\n" , lt, " ", rt)

	x=func_permutation(rt,ep)
	print("After expansion/permutation\n", x)

	for i in range(8):
		if x[i]==key[i]:
			x[i]="0"
		else:
			x[i]="1"
	print("After First xor(with Key)\n", x)

	lx=x[:4].copy()
	rx=x[4:].copy()
	print("Left and Right\n", lx, " ", rx)

	s0=[["01","00","11","10"],
	["11","10","01","00"],
	["00","10","01","11"],
	["11","01","11","10"]]

	s1=[["00","01","10","11"],
	["10","00","01","11"],
	["11","00","01","00"],
	["10","01","00","11"]]

	d={"00":0,"01":1,"10":2,"11":3}

	r1=lx[0]+lx[3]
	c1=lx[1]+lx[2] 
	r2=rx[0]+rx[3]
	c2=rx[1]+rx[2]
	print("Row, Col", r1, c1, r2, c2)

	l=s0[d[r1]][d[c1]]
	r=s1[d[r2]][d[c2]]
	print("After s0 s1\n", l, " ", r)

	x = list(l+r)
	print("Before P4\n", x)

	x=func_permutation(x,p4)
	print("After P4\n", x)

	for i in range(4):
		if x[i]==lt[i]:
			x[i]="0"
		else:
			x[i]="1"

	if f == 1:
		x=rt+x
	else:
		x=x+rt
	return x

p10=[3,5,2,7,4,10,1,9,8,6]
p8=[6,3,7,4,8,5,10,9]
ip8=[2,6,3,1,4,8,5,7]
ipinv=[4,1,3,5,7,2,8,6]

key=list(input("Enter 10 bit key : "))						# [1010000010, 01110010]
key=func_permutation(key,p10)
print("After applying P10 permutation:\n", key)

left_key = key[:5].copy()
right_key = key[5:].copy()
print("After Split:\n", left_key, " ", right_key)

left_key.append(left_key[0])
del left_key[0]
right_key.append(right_key[0])
del right_key[0]
print("After shift operation:\n", left_key, " ", right_key)

key1 = left_key + right_key
key1=func_permutation(key1,p8)
print("Subkey 1:\n", key1)

left_key.append(left_key[0])
left_key.append(left_key[1])
del left_key[0]
del left_key[0]
right_key.append(right_key[0])
right_key.append(right_key[1])
del right_key[0]
del right_key[0]
print("After two left shift operation:\n", left_key, " ", right_key)

key2 = left_key + right_key
key2=func_permutation(key2,p8)
print("Subkey2:\n", key2)
print("SubKey1 :","".join(key1),"\nSubKey2 :","".join(key2))

txt = list(input("Enter 8 bit Plain-text : "))

txt=func_permutation(txt,ip8)
print("After ip8 permutation\n", txt)

txt1 = func_encryption(txt,key1,1)
print("Encryption using K1\n", txt1)

txt2 = func_encryption(txt1,key2,0)
print("Encryption using K2\n", txt2)


cpht=func_permutation(txt2,ipinv)
print("Encrypted text :","".join(cpht))

cpht=func_permutation(cpht,ip8)
dtxt1 = func_encryption(cpht, key2, 1)
dtxt2 = func_encryption(dtxt1, key1, 0)
op=func_permutation(dtxt2,ipinv)
print("Original Plain-Text",op)