function promisify(callback) {
  // Write your code here.
  return function (...args) {
    return new Promise((resolve, reject) => {
      function errorHandler(err, value) {
        if (err) {
          return reject(err);
        } else {
          return resolve(value);
        }
      }
      return callback.apply(this, [...args, errorHandler]);
    });
  };
}
