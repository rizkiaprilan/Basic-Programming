// *
// **
// ***
// ****
// *****
var a = ''
for (var i = 1; i <= 5; i++) {
    for (var j = 1; j <= i; j++) {
        a += '*'
    }
    a += '\n'
}
console.log(a)

// *****
// ****
// ***
// **
// *
var a = ''
for (var i = 5; i >= 1; i--) {
    for (var j = 1; j <= i; j++) {
        a += '*'
    }
    a += '\n'
}
console.log(a)

//     *
//    **
//   ***
//  ****
// *****
var a = ''
var q = 1
for (var i = 5; i >= 1; i--) {
    for (var j = 1; j < i; j++) {
        a += ' '
    }
    for (var k = 1; k <= q; k++) {
        a += '*'
    }
    q++
    a += '\n'
}
console.log(a)
// *****
//  ****
//   ***
//    **
//     *
var a = ''
var q = 5
for (var i = 1; i <= 5; i++) {
    for (var j = 1; j < i; j++) {
        a += ' '
    }
    for (var k = 1; k <= q; k++) {
        a += '*'
    }
    q--
    a += '\n'
}
console.log(a)