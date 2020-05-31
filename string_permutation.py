s = 'abcde'

def permute(s):
    q = []
    q.append(s[0])
    
    current_index = 1
    while(len(q) != 0):
        element = q.pop()
        if(len(element) == len(s)):
            break
        for i in range(0, len(element) + 1):
            newPermutation = element[:i] + s[current_index] + element[i:]
            q.append(newPermutation)
            print (newPermutation)

        current_index += 1

permute(s)