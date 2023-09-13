function solution(my_string) {
    let answer = 0;
    let num = my_string.split('')
    
    for ( i = 0; i < my_string.length; i++){
        if (Number(num[i])) {
            answer += parseInt(num[i])
        }
    }
    
    return answer;
}