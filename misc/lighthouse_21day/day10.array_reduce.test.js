const averageWindSpeed = weatherEntries => Math.round(
  weatherEntries.reduce((prev, curr) => prev + curr.windSpeed, 0)
  / weatherEntries.length
)
/*
The reduce() method executes a user-supplied “reducer” callback function on each element
of the array, in order, passing in the return value from the calculation on the preceding
element. The final result of running the reducer across all elements of the array is a
single value.
*/
const exampleEntries = [
  { 
    temperature:0, 
    weather:"sunny", 
    windDirection: "NNE", 
    windSpeed:24
  },
  { 
    temperature:10, 
    weather:"cloudy", 
    windDirection: "NNE", 
    windSpeed:9 
  }
]

test('function takes an array of objects and returns the average wind speed', () => {
  expect(averageWindSpeed(exampleEntries)).toBe(17)
})