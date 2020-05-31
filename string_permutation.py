s = 'abc'

def permute(s):
    q = []
    q.append(s[0])
    
    while(len(q) != 0):
        element = q.pop(0)
        if(len(element) == len(s)):
            break
        current_index = len(element)
        for i in range(0, len(element) + 1):
            newPermutation = element[:i] + s[current_index] + element[i:]
            q.append(newPermutation)
    return q

print(permute(s))