var again = true

while (again) {
    var input = prompt("pilih[batu, gunting, kertas]: ")
    var random = Math.random()  //random dari 0 - 1
    var hasil = ''
    if (random < 0.34) {
        random = 'batu'
        if (input == random) {
            hasil = 'SERI'
        } else {
            hasil = input == 'gunting' ? 'KALAH' : 'MENANG'
            hasil = input == 'kertas' ? 'MENANG' : 'KALAH'
        }
    } else if (random >= 0.34 && random < 0.67) {
        random = 'gunting'
        if (input == random) {
            hasil = 'SERI'
        } else {
            hasil = input == 'kertas' ? 'KALAH' : 'MENANG'
            hasil = input == 'batu' ? 'MENANG' : 'KALAH'
        }
    } else if(random >= 0.67){
        random = 'kertas'
        if (input == random) {
            hasil = 'SERI'
        } else {
            hasil = input == 'batu' ? 'KALAH' : 'MENANG'
            hasil = input == 'gunting' ? 'MENANG' : 'KALAH'
        }
    }

    again = confirm('komputer memilih: ' + random + '\nkamu memilih: ' + input + '\nmaka hasilnya: ' + hasil+ '\nmau main lg?')
    
}
alert('terima kasih sudah bermain')