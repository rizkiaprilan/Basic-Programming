alert('liat consolenya ya')

var jmlAngkot = 10
var nomorAngkot = 1
var angkotBeroperasi = 6
while (nomorAngkot <= jmlAngkot) {
    if (nomorAngkot <= angkotBeroperasi && nomorAngkot != 5) {
        console.log('Angkot No.' + nomorAngkot + ' beroperasi dengan baik')
    } else {
        if (nomorAngkot % 2 == 0) {
            console.log('Angkot No.' + nomorAngkot + ' sedang lembur')
        } else {
            console.log('Angkot No.' + nomorAngkot + ' sedang tidak beroperasi')
        }
    }
    nomorAngkot++
}