function solution(s) {
    let arr = s.split('')
    let sorted = arr.sort().reverse()
    
    return sorted.join('')
}