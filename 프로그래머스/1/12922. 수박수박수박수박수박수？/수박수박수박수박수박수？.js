function solution(n) {
    let watermelon = [];
    
    for ( i = 0; i < n; i++ ) {
        
        if ((i + 1) % 2 === 0) {
            watermelon[i] = '박'
        } else {
            watermelon[i] = '수'
        }
        
    }
    
    return watermelon.join('');
}