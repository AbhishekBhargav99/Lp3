from hashlib import new
import numpy as np;

p10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6];
p8 = [6, 3, 7, 4, 8, 5, 10, 9];
IP = [ 2, 6, 3, 1, 4, 8, 5, 7 ];
EP = [ 4, 1, 2, 3, 2, 3, 4, 1 ];
P4 = [ 2, 4, 3, 1 ];
IP_inv = [ 4, 1, 3, 5, 7, 2, 8, 6 ];

S0 =  [ [ 1, 0, 3, 2 ],
        [ 3, 2, 1, 0 ],
        [ 0, 2, 1, 3],
        [ 3, 1, 3, 2 ] ];

S1 =  [ [ 0, 1, 2, 3 ],
        [ 2, 0, 1, 3 ],
        [ 3, 0, 1, 0 ],
        [ 2, 1, 0, 3 ] ];

def left_shift(number, bits):
    newNum = np.roll(number, -bits);
    return newNum;

def permute(key, combination):
    newKey = [];
    for i in combination:
        index = i - 1;
        newKey.append(key[index]);
    return newKey;

# 1010000010
# 10010111
def generate_key(newKey):
    
    key = permute(newKey, p10);
    ls1 = left_shift(key[0:5], 1);
    rs1 = left_shift(key[5:], 1);
    c1 = np.append(ls1, rs1);
    k1 = permute(c1, p8);

    ls2 = left_shift(ls1, 2);
    rs2 = left_shift(rs1, 2);
    c2 = np.append(ls2, rs2);
    k2 = permute(c2, p8)
    return k1, k2;

def sBox(block, s):
    row = 2 * block[0] + block[3];
    col = 2 * block[1] + block[2];
    print(row, col);
    val1 = s[row][col];
    print('val1 : ', val1)
    op = [];
    while val1:
        op.append(val1%2);
        val1 = val1 // 2;
    return op[::-1];
    
    

def perform_Fk(rb, key):
    ep = [];
    for i in EP:
        ep.append(rb[i - 1]);
    print('Expansion Perutation : ', ep);
    ebo = []
    for i,j in zip(ep, key):
        ebo.append(int(i) ^ int(j));
    print('key xor ep : ', ebo);
    lb = ebo[0:4]
    rb = ebo[4:];
    s0 = sBox(lb, S0)
    s1 = sBox(rb, S1)
    c = np.append(s0, s1);
    p4 = permute(c, P4);
    return p4;
    


def encrypt(plainText, key1, key2):
    ip8 = permute(plainText, IP);
    print('IP8 : ', ip8);
    lb1 = ip8[0:4];
    rb1 = ip8[4:];
    p4 = perform_Fk(rb1, key1);

    lb2 = rb1;
    rbTemp = [];
    for a, b in zip(lb1, p4):
        rbTemp.append(int(a) ^ int(b));
    rb2 = [];
    for el in rbTemp:
        rb2.append(str(el));
    print('p4: ',p4);
    print('lb2 : ', lb2);
    print('rb2 : ', rb2);
    
    p42 = perform_Fk(rb2, key2);
    
    rb3 = rb2;
    rbTemp = [];
    for a, b in zip(lb2, p42):
        rbTemp.append(int(a) ^ int(b));
    lb3 = [];
    for el in rbTemp:
        lb3.append(str(el));
    print('p42: ',p42);
    print('lb3 : ', lb3);
    print('rb3 : ', rb3);

    combo = np.append(lb3, rb3);
    cipherText = permute(combo, IP_inv);
    return cipherText;





# key = list(input("Enter 10 bit key : "));
# plainText = list(input('Enter 8 bit Plain Text : '));

key = list('1010000010');
plainText = list('10010111');

key1, key2 = generate_key(key);
print('Key - 1 :', key1 )
print('Key - 2 :', key2 )

cipherText = encrypt(plainText, key1, key2);
print('Cipher Text : ', cipherText);