function penjumlahan(a, b) {
  return a + b;
}

function pengurangan(a, b) {
  return a - b;
}

var again = true;
while (again) {
  var nilai1 = parseInt(prompt("masukkan nilai 1: "));
  var nilai2 = parseInt(prompt("masukkan nilai 2: "));

  alert(
    "\nhasil penjumlahan: " +
      penjumlahan(nilai1, nilai2) +
      "\nhasil pengurangan: " +
      pengurangan(nilai1, nilai2)
  );
  again = confirm("try again?");
}

//================================================================================================
function tambah() {
  //sudo variable argument-> parameter tak ditentukan, argumentnya bebas
  var hasil = 0;
  for (var i = 0; i < arguments.length; i++) {
    hasil += arguments[i];
  }
  return hasil;
}

alert(tambah(1, 4, 5, 7, 9)); //angka tersbut di bilang argument

//========================================functionExpression=======================================

var tampilPesan = function(nama) {
  alert("halo " + nama);
};

tampilPesan("rizki");

console.log(typeof(tampilPesan))  
