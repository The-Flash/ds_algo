function twoNumberSum(array, targetSum) {
    array.sort((a, b) => a - b);
    let i = 0;
    let j = array.length - 1;
    while (i < j) {
        let lNum = array[i];
        let rNum = array[j];
        let sum = lNum + rNum;
        if (sum === targetSum) {
            return [lNum, rNum];
        }
        if (sum > targetSum) {
            j--;
        }
        if (sum < targetSum) {
            i++;
        }
    }
    return []
}

