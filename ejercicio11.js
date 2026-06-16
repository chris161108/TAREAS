// succesion de fibonacci 

let n1 = 0, n2 = 1, siguiente;

for (let i = 1; i <= 15; i++) {
    console.log(n1);
    siguiente = n1 + n2;
    n1 = n2;
    n2 = siguiente;
}