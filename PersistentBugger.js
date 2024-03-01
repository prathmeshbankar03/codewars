function persistence(num) {
    if (num.toString().length === 1) {
        return 0;
    }
    var mult = 1;
    var splitStr = num.toString().split("");
    for (var i = 0; i < splitStr.length; i++) {
        mult *= parseFloat(splitStr[i])
    }
    return 1 + persistence(parseFloat(mult));
}

console.log(
    persistence(999),
    persistence(39),
    persistence(4)
);