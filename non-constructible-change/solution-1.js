function nonConstructibleChange(coins) {
    // Write your code here.
    let change = 0;
    if (coins.length === 0) {
        return 1;
    }
    coins.sort((a, b) => a - b);
    for (let coin of coins) {
        if (coin > (change + 1)) {
            break;
        }
        change += coin;
    }
    return change + 1;
}

// Do not edit the line below.
exports.nonConstructibleChange = nonConstructibleChange;
