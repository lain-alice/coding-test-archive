function cal_gcd(a, b) {
    return a % b === 0 ? b : cal_gcd(b, a % b)
    // a를 b로 나눴을 때 나머지가 0이면 b가 최대공약수
    // 0이 아니면 a를 a와 b의 나머지로 나눈다, 계속 나눠서 0이 되면 나머지가 최대공약수
    // 재귀?
}

function solution(numer1, denom1, numer2, denom2) {
    let denum = numer1 * denom2 + numer2 * denom1;
    // 통분... 분자 합: 분자에 상대 분모 곱해서 더함
    let num = denom1 * denom2;
    // 분모 합: 분모끼리 곱하기
    let gcd = cal_gcd(denum, num);
    
    return [denum / gcd, num / gcd];
    // 분모 곱 통분해서 더한 다음 분자 분모를 최대공약수로 나눈다
}