function solution(array) {
    
    array.sort((a, b) => a - b);
    
    let middle = parseInt((array.length - 1) / 2)
    
    return array[middle];
}