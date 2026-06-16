// conjetura de collatz 

let n = 6;

console.log("inicio con :" + n);
while (n !== 1) {
    if (n % 2 === 0) {
        n = n / 2;
    } else {
        n = n * 3 + 1;
    }
    console.log(n);
}