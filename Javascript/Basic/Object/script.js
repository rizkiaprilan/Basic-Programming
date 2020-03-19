// object

var dataDiri = {
    nama: 'rizki aprilan',              //properti
    umur: 20,
    ips: [3.00, 4.00, 3.13, 3.19],
    alamat: {
        jalan: "jl. nimun raya",
        kota: 'jakarta selatan',
        provinsi: 'DKI jakarta'
    },
    halo: function(){
        console.log('hallo')
    }

}

console.log(dataDiri)

function createObjectMahasiswa(nama, NIM, email, jurusan) {
    var mhs = {};
    mhs.nama = nama;
    mhs.NIM = NIM;
    mhs.email = email;
    mhs.jurusan = jurusan;
    return mhs;
}

var mhs1 = createObjectMahasiswa('rizki', '2101713033', 'rizki@gmail.com', 'teknik informatika')


//constructor
function Mahasiswa(nama, NIM, email, jurusan) {  //umumnya pake huruf besar di awal
    // var this = {}
    this.nama = nama;
    this.NIM = NIM;
    this.email = email;
    this.jurusan = jurusan;

    //return this
}
var mhs2 = new Mahasiswa('budi','123123133','sadasdas@sfsa.com','pangan');//harus pake new

//==============================
//function didalam object
var obj = {};
obj.halo = function(){
    console.log('hallo')
}
obj.halo()

//===============================
var obj2 = {
    a: 10,
    nama: 'rizki'
}
obj.halo2 = function(){
    console.log(this); //this mengembalikan object yang bersangkutan
    console.log('halo');
}
obj.halo();

console.log(this) //this mengembalikan object global