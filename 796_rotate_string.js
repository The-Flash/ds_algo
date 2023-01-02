const rotateString = function(A, B) {
    if(A.length !== B.length) return false;
    if(A.length === 0 && B.length === 0) return true;
    A = A + A;
    let i = 0;
    let j = B.length;
    while(i + j < A.length) {
        let subStr = A.substring(i, i + j);
        if(subStr === B) {
            return true;
        }
        i++;
    }
    return false;
}

let A, B, result;

A = "abcde"; B="cdeab";

result = rotateString(A, B);
console.log(result);

A = "abcde"; B="abced";

result = rotateString(A, B);
console.log(result);