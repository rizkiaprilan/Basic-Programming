/**
 * cara menjalankan node js => lokasi directory dari file, kemudian node [nama javascript]
 */



console.log("==========================================")

var nama = "rizki";
console.log("Nama saya", nama, "dan umur saya", 21);

console.log("==========================================")

if (nama == "rizki") {
    console.log("benar")
} else {
    console.log("salah")
}

console.log("==========================================")

var Angka = 18
var mod = Angka % 2
switch (mod) {
    case 0:
        console.log('genap')
        break
    case 1:
        console.log('ganjil')
        break
    default:
        console.log('bukan angka')
        break
}

console.log("==========================================")

for (var i = 0; i < 3; i++) {
    console.log(i)
}

console.log("==========================================")

var a = 3
var b = 0
while (b < a) {
    console.log(b)
    b++
}

console.log("==========================================")

var json = [{
    name: "rizki",
    umur: 23,
    buku: [
        "naruto",
        "onepiece"
    ]
}, {
    name: "jamet",
    umur: 29,
    buku: [
        "onepunchman"
    ]
}]

console.log(json[0].buku[1])

console.log("==========================================")

var myObj = [{
    name: "rizki",
    age: 21,
    profil: function() {
        console.log("nama saya", this.name, "dan umur saya", this.age)
    }
}]

myObj[0].profil()

console.log("==========================================")

var math = require("../Moduls/math.js")
console.log("hasilnya penambahan adalah", math.tambah(1, 2, 4))
console.log("hasilnya pengurangan adalah", math.kurang(1, 2, 4))
console.log("hasilnya perkalian adalah", math.kali(1, 2, 4))

console.log("==========================================")

var math_obj_factory = require("../Moduls/math_obj_factory.js")

var math_obj1 = math_obj_factory() //inisialisasi objek factorynya
math_obj1.materi = "trigonometri" //set
console.log(math_obj1.materi)
var math_obj2 = math_obj_factory() //inisialisasi objek factorynya
math_obj2.materi = "algoritma" //set
console.log(math_obj2.materi)