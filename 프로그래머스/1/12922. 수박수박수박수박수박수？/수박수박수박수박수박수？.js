function solution(n) {
    let watermelon = '';
    
    for ( i = 0; i < n; i++ ) {        
        ((i + 1) % 2 === 0) ? watermelon += '박' : watermelon += '수';
    }
    
    return watermelon;
}