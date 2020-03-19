function cetakAngka(n) {
    if (n == 0) {
        return  //untuk berhenti
    }
    console.log(n)
    cetakAngka(n - 1)
}

cetakAngka(20)

//==================factorial===================

function factorial(a){
    if(a == 0) return 1

    return a * factorial(a-1)
}

console.log(factorial(5 ))