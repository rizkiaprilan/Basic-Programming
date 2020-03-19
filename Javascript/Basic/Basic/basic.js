alert("HELLO GUYS");  //untuk popup message di browser, bisa ketik di console

//exponen
// 123e5  -> 12300000
// 123e-5 -> 0.00123

//perbandingan
//===  -> membanding kan 2 operand beserta tipe datanya juga

var x = 15;
var y = "15";

//FOR

for(var i=1;i<=5;i++){
    alert('angka: ' + i);
}

console.log((x % 0 == 0) ? "genap" : "ganjil");  //akan di tampilkan di console

//POPUP BOXs
// alert(x === y); 
// var nama = prompt("masukkan nama: ");  
// alert(nama);

// if(confirm("yakinn") == true){  
//     alert("user menekan tombol ok")
// }else{
//     alert('user menekan tombol cencel')
// }

alert("selamat datang web html ini")  //popup window kecil

var lagi = true;

while(lagi){
    var nama = prompt('siapa nama mu?')   //akan meminta inputan dari user, dan returnnya string
    var umur = prompt('umur mu?')

    alert('nama: ' + nama + '\numur: ' + umur);
    lagi = confirm('mau perkenalkan lagi?')  //Returnnya boolean
}

alert('terima kasih atas waktunya')

//BUILT-IN Function -> function yang sudah di sediakan javascript

