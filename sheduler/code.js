//SetTimeout

let a = 0
console.log("A")
let id = setTimeout(() => {
    console.log("B")
}, 3000)
console.log("K")
let idi = setTimeout(() => {
    console.log("Himashi")
}, 1000)

//SetInterval
let count = 0
let p = setInterval(() => {
    console.log(count)
    count++

    if (count > 10) {
        clearInterval(p)
    }
}, 1000)