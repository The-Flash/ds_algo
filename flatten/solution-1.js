function flatten(value) {
    if (isPrimitive(value)) {
        return value;
    }

    if (Array.isArray(value)) {
        return flattenArray(value);
    }

    return flattenObject(value);
}

/**
 * @param {Array} value
 */
function flattenArray(value) {
    return value.reduce((acc, curr) => acc.concat(flatten(curr)), []);
}

function flattenObject(value) {
    let result = {};
    for (let [k, v] of Object.entries(value)) {
        if (isPrimitive(v) || Array.isArray(v)) {
            result[k] = flatten(v);
        } else {
            //   result = { ...result, ...flattenObject(v) };
            Object.assign(result, flatten(v));
        }
    }
    return result;
}

function isPrimitive(value) {
    return typeof value !== "object" || value === null;
}
