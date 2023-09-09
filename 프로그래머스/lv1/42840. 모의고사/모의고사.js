function solution(answers) {
        
    let answer = [];
    let dumb1 = [1, 2, 3, 4, 5];
    let dumb2 = [2, 1, 2, 3, 2, 4, 2, 5];
    let dumb3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    
    const correct1 = answers.filter((a, i)=> a === dumb1[i % dumb1.length]).length;
    const correct2 = answers.filter((a, i)=> a === dumb2[i % dumb2.length]).length;
    const correct3 = answers.filter((a, i)=> a === dumb3[i % dumb3.length]).length;
    
    const max = Math.max(correct1, correct2, correct3);

    if (correct1 === max) {answer.push(1)};
    if (correct2 === max) {answer.push(2)};
    if (correct3 === max) {answer.push(3)};   
    
    return answer;
}