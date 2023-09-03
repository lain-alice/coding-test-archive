function solution(arr) {
    let answer = [];
    
    for ( i = 0; i < arr.length; i++ ){
        if ( arr[i] !== arr[i + 1] ) answer.push(arr[i]);
        // 앞 원소가 뒤 원소랑 다를 때만 answer 배열에 arr의 원소들을 넣는다
    }    
    
    
    return answer;
}