function solution(a, b) {
    let sum = 0;
    
    for (i = 1; i <= a.length; i++) {
        sum += a[i - 1] * b[i - 1];
    }
    
    return sum;
}