function isValidSubsequence(array, sequence) {
    let r = [];
    let i = 0;
    for (let v of array) {
        if (v === sequence[i]) {
            r.push(v);
            i++
        }
    }
    return r.length === sequence.length;
}
