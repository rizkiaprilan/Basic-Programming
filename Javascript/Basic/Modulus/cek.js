var again = true
while (again) {
    var angka = prompt('masukkan angka: ')

    if (angka % 2 == 0) {
        alert('angka genap')
    } else if(angka % 2 == 1){
        alert('angka ganjil')
    }else{
        alert('bukan angka / bilangan bulat')
    }
    again = confirm('mau cek lg?')
}