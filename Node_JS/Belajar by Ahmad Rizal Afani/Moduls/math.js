module.exports = { //export agar bisa di akses file lain
    tambah: function() {
        var hasil = 0
        for (var i = 0; i < arguments.length; i++) {
            hasil += arguments[i]
        }
        return hasil
    },

    kurang: function() {
        var hasil = 0
        for (var i = 0; i < arguments.length; i++) {
            hasil -= arguments[i]
        }
        return hasil
    }
}

//===========================================

//Cara 2
var perkalian = function() {
    var hasil = 1
    for (var i = 0; i < arguments.length; i++) {
        hasil *= arguments[i]
    }
    return hasil
}
module.exports.kali = perkalian

//===========================================