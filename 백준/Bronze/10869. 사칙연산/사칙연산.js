const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split(' ');

const a = parseInt(input[0]);
const b = parseInt(input[1]);

let plus = a + b;
let minus = a - b;
let multiple = a * b;
let divide = parseInt(a / b);
let remainder = a % b;

console.log(`${plus}
${minus}
${multiple}
${divide}
${remainder}
`)
