s = 'abc'

def permute(s):
    q = []
    q.append(s[0])
    
    while(len(q) != 0):
        if(len(q[0]) == len(s)):
            break
        element = q.pop(0)
        current_index = len(element)
        for i in range(0, len(element) + 1):
            newPermutation = element[:i] + s[current_index] + element[i:]
            q.append(newPermutation)
    return q

print(permute(s))
permutations = permute('abcd')
print(len(permutations), permutations)