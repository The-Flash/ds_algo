function twoNumberSum(array, targetSum) {
    // Write your code here.
    let map = {}
    for(let x of array) {
      // x + y = 10
      // y = 10 - x
      let y = targetSum - x;
      if(map[y]) {
        return [x, y];
      }
      map[x] = true;
    }
    return []
  }
  
  // Do not edit the line below.
  exports.twoNumberSum = twoNumberSum;
  