function solution(n) {
    let arr = String(n).split('')
    
    
    let answer = arr.map((a) => parseInt(a)).reduce((prev, cur) => {
                
        return prev + cur
               
    });
        
    return answer;
}