def solution(s):
    answer = []
    words = s.split(' ')
    
    for word in words:
        new = ''        
        for i in range(len(word)):
            new += word[i].upper() if i % 2 == 0 else word[i].lower()
        answer.append(new)
            
    return " ".join(answer)