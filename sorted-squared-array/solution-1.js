function sortedSquaredArray(array) {
    let output = new Array(array.length);
    let startIndex = 0;
    let endIndex = array.length - 1;
    let i = array.length - 1;

    while (i >= 0) {
        let start = array[startIndex]
        let end = array[endIndex];

        if (Math.abs(start) < Math.abs(end)) {
            output[i] = end ** 2;
            endIndex--;
        } else {
            output[i] = start ** 2;
            startIndex++;
        }
        i--;
    }
    return output;
}

