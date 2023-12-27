const assert = require("node:assert")

function deepEquals(valueOne, valueTwo) {
    if (typeof valueOne !== typeof valueTwo) {
        return false;
    }
    if (typeof valueOne !== "object") {
        if (Number.isNaN(valueOne) && Number.isNaN(valueTwo)) {
            return true;
        }
        return valueOne === valueTwo;
    }
    if (valueOne === null || valueTwo === null) {
        return valueOne === valueTwo;
    }
    if (valueOne === valueTwo) {
        return true;
    }
    if (Array.isArray(valueOne) && Array.isArray(valueTwo)) {
        if (valueOne.length !== valueTwo.length) {
            return false;
        }
        for (let i = 0; i < valueOne.length; i++) {
            if (!deepEquals(valueOne[i], valueTwo[i])) {
                return false;
            }
        }
        return true;
    }
    if (Array.isArray(valueOne) || Array.isArray(valueTwo)) {
        return false;
    }
    const valueOneKeys = Object.keys(valueOne);
    const valueTwoKeys = Object.keys(valueTwo);
    if (valueOneKeys.length !== valueTwoKeys.length) {
        return false;
    }
    for (const key of valueOneKeys) {
        if (!valueTwo.hasOwnProperty(key)) {
            return false
        }
        if (!deepEquals(valueOneKeys[key], valueTwoKeys[key])) {
            return false
        }
    }
    return true;
}

assert.equal(deepEquals(1, 1), true);
assert.equal(deepEquals([], []), true);
assert.equal(deepEquals([1, 2, 4,], [1, 2, 4,]), true);
assert.equal(deepEquals({}, {}), true);
assert.equal(deepEquals({ a: 1 }, { b: 1 }), false);
assert.equal(deepEquals({ a: 1 }, { a: 1 }), true);
assert.equal(deepEquals({ a: 1, b: [] }, { a: 1 }), false);
assert.equal(deepEquals({ a: 1, b: [] }, { a: 1, b: [] }), true);