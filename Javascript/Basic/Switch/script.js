var again = true
while (again) {

    var angka = parseInt(prompt('masukkan angka: ')) //ubah tipe datanya menjadi integer
    var mod = angka % 2
    switch (mod) {
        case 0:
            alert('genap')
            break
        case 1:
            alert('ganjil')
            break
        default:
            alert('bukan angka')
            break
    }
    again = confirm('mau cek lg?')
}