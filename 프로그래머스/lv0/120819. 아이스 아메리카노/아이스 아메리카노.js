function solution(money) {
    let answer = [];
    let americano = parseInt(money / 5500);
    let change = money % 5500;
    answer = [americano, change]
    
    return answer;
}