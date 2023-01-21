const testCases = []
function describe(testSuiteName, func) {
  // Write your code here.
  console.log(`beginning test suite ${testSuiteName}`);
  func();
  for(let testCase of testCases) {
    const testCaseName = testCase["name"];
    const testCaseFunc = testCase["func"];
    console.log(`beginning test case ${testCaseName}`);
    try {
        testCaseFunc();
        console.log(`${testCaseName} \npassed`);
    } catch(error) {
        console.error(`${testCaseName} \nfailed: ${error}`);
    }
  }
}

function it(testCaseName, func) {
  // Write your code here.
  testCases.push({
    name: testCaseName,
    func
  });
}

function expect(actual) {
  // Write your code here.
  const stringifiedActual = JSON.stringify(actual);
  return {
    toExist: function() {
      if(actual == null) {
        throw `expected ${actual} to exist but got ${stringifiedActual}`;
      }
    },
    toBe: function(expected) {
      if(actual !== expected) {
        throw `expected ${stringifiedActual} to be ${JSON.stringify(expected)}`;
      }
    },
    toBeType: function(expectedType) {
      const type = typeof actual;
      if(type !== expectedType) {
        throw `expected ${this.stringifiedActual} to be of type ${expectedType} but got ${type}`;
      }
    }
  }
}
describe("T", function() {
    it("Expect '2' to be '2'", function() {
        expect(2).toBe(2);
    })
    
    it("Expect '2' to be '6'", function() {
        expect(2).toBe(6);
    })

    it("Expect 'hello' to be a 'string'", function() {
        expect("hello").toBeType("string");
    })

    it("Expect '{}' to not exist", function() {
        expect({}).toExist()
    })
})
