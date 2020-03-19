function Angkot(sopir, trayek, penumpang, kas) {  //membuat object angkot
    this.sopir = sopir;
    this.trayek = trayek;
    this.penumpang = penumpang;
    this.kas = kas;
    this.penumpangNaik = function (namaPenumpang) {
        this.penumpang.push(namaPenumpang)
        return this.penumpang;
    }
    this.penumpang = function(namaPenumpang,bayar){
        if(this.penumpang.length === 0){
            alert('angkot masih kosong!');
            return false;
        }

        for(var i = 0;i<this.penumpang.length;i++){
            if(this.penumpang[i] == namaPenumpang){
                this.penumpang[i] = undefined; //dihapus
                this.kas += bayar;
                return this.penumpang;
            }
        }
    }
}

var angkot1 = new Angkot('rizki', ['kebayoran', 'blok M', 'sisingamangaraja'], [], 0);
var angkot2 = new Angkot('budi', ['Gandaria', 'blok A','PIM'], [], 0);