function solution(lottos, win_nums) {
        
    let sameNums = lottos.filter( a => win_nums.includes(a) )
    let erasedNums = lottos.filter( a => a === 0 )
    
    let minRank = 0
    let maxRank = 0
    
    if (sameNums.length <= 1) {
        minRank = 6
    } else {
        minRank = 7 - sameNums.length
    } 
    
    if (sameNums.length <= 1 && erasedNums.length === 0) {
        maxRank = 6
    } else {
        maxRank = 7 - (sameNums.length + erasedNums.length)
    } 
    
    let answer = [];
    answer.push(maxRank, minRank)
    
    return answer;
}