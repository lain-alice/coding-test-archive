function solution(s) {
    
    let word = s.split(' ')
    
    let answer = []
    
    
    for ( i = 0; i < word.length; i++ ) { 
        
        let newWord = ''
                                        
        for ( j = 0; j < word[i].length; j++ ) {                     
            
            if ( j === 0 || j % 2 === 0) {                
                                           
                newWord += word[i][j].toUpperCase()               
                                
            } else {
                
                newWord += word[i][j].toLowerCase()
            }                  
        }              

        answer.push(newWord)
         
    }
        
    
    return answer.join(' ');
}