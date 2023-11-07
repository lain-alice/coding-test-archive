const fs = require('fs');
const y = fs.readFileSync('/dev/stdin').toString().trim();

console.log(`${y - 543} `);

