function solution(array, height) {
    let answer = 0;
    
    let taller = array.filter((el) => el > height);
    
    answer = taller.length;
    
    return answer;
}