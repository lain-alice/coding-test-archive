function solution(food) {
    
    let table = '';
    
    for ( i = 1 ; i <= food.length ; i++ ){
        
        let count = Math.floor(food[i] / 2)        
        table += String(i).repeat(count)        
        
    }
    
    let answer = table + '0' + [...table].reverse().join('')
    
    return answer;
}