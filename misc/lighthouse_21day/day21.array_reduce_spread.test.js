const parseMissionSummary = (exchanges, missionData) => {
  return {
    transcript: exchanges.reduce((p, c) => [...p, `${c.origin}: ${c.message}`], []),
    missionData
  }
}
/*
Spread syntax (...) allows an iterable such as an array expression or string to be
expanded in places where zero or more arguments (for function calls) or elements (for
array literals) are expected, or an object expression to be expanded in places where
zero or more key-value pairs (for object literals) are expected.

function sum(x, y, z) {
  return x + y + z;
}
const numbers = [1, 2, 3];
console.log(sum(...numbers));
// expected output: 6
console.log(sum.apply(null, numbers));
// expected output: 6
*/

const exchanges = [
  {origin:"MC", message:"So how is it out there?"},
  {origin:"Shuttle", message:"Oh it's pretty nice!"},
  {origin:"MC", message:"Did you like the challenges?"},
]  
const missionData = {a:1}

test('summerize list of objects in exchanges to list of strings in transcript', () => {
  expect(parseMissionSummary(exchanges, missionData)).toStrictEqual({
    transcript: [
      "MC: So how is it out there?",
      "Shuttle: Oh it's pretty nice!",
      "MC: Did you like the challenges?"
    ],
    missionData: {a:1}
  })
})