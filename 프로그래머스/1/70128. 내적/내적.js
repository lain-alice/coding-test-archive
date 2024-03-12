function solution(a, b) {
    let multiple = [];
    
    for (i = 1; i <= a.length; i++) {
        multiple.push(a[i - 1] * b[i - 1]);
    }
        
    let sum = multiple.reduce((prev, cur) => prev + cur);
    
    return sum;
}