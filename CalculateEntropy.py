from math import log2

def CalculateEntropy(penis):
    entropy = []
    for p in penis:
        val = 0
        if p > 0:
            val = p*log2(p)
            #print(val)
        entropy.append(val)
    #print(min(entropy))
    entropy = sum(entropy)
    entropy *= -1
    return entropy

A = [0.044, 0.022, 0.78, 0, 0.14, 0.011]
B = [0, 0.11, 0, 0.77, 0.021, 0.11]

print(CalculateEntropy(A))
print(CalculateEntropy(B))

#out of curiousity I ran this code to find what value of P gives the maximum value of entropy, 0.37 seems to be the answer for some reason? with entropy = 0.530737
#ah, yeah its maximised at p = 1/e 
l = range(100)
l = [i/100 for i in l]
#print(CalculateEntropy(l))