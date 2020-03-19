
var hari = ['senin', 'selasa', 'rabu', 'kamis', 'jum\'at', 'sabtu', 'minggu']   //array tipedatanya itu object
var myArr = ['rizki', 20, true, [4, 5, 6]];  //semua type data bisa disimpan di array, termasuk function
var mhs = ['rizki', 'sahlan', 'salsa', 'budi']
var angka = [1, 2, 3, 4, 5, 6, 7]
var acak = [20, 11, 1, 5, 3, 7, 9, 4]

//cara 1
for (var i = 0; i < hari.length; i++) {
    console.log(hari[i])
}

//cara 2
mhs.forEach(function (e, i) {   //cara function expression
    console.log('mahasiswa ke-' + i + ' adalah ' + e)
})

//MAP
var angka2 = angka.map(function (e) {
    return e * 2
})
console.log(angka2.join(' - '))  //2 - 4 - 6 - 8 - 10 - 12 - 14


//SORT
console.log(acak.sort())   //sorting
console.log(acak.sort(function (a, b) {      //sorting cara 2
    return a - b
}))


//FILTER
var filter = acak.filter(function (e) { 
    return e > 5        //menacari banyak nilai sesuai kondisi yaitu 7,9,11,20
})
console.log(filter)

var filter = acak.find(function (e) { 
    return e > 5        //mencari satu nilai pertama ketemu, 7
})
console.log(filter)



//PUSH
var again = true
while (again) {
    var mahasiswa = prompt('masukkan nama mahasiswa: ')
    mhs.push(mahasiswa)   //menambahkan elemen dari belakang
    console.log(mahasiswa)

    again = confirm("try again? ")
}

hari[1] = undefined  //untuk menghapus


//POP
hari.pop();              // untuk menghapus dari belakang 
console.log(hari)


//UNSHIFT
hari.unshift('test123')  //menambah elemen dari depan
console.log(hari)


//SHIFT
hari.shift()             //menghapus elemen dari depan
console.log(hari)


//SPLICE
mhs.splice(2, 0, 'andri', 'willy')   //splice(indexAwal, mauDihapusBerapa, elemenBaru1(opt), elemenBaru2(opt), ...)
console.log(mhs)


//SLICE
var mhs2 = mhs.slice(1, 3)  //slice(indexAwal,indexAkhir)  indexAkhir tidak dimasuk slicing
console.log(mhs2)


//JOIN
console.log(hari.join(' - '))  //mengubah elemennya menjadi string, argumentnya itu adalah separatornya 