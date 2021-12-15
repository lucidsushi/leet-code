/* The map() method creates a new array populated with the results of calling a
provided function on every element in the calling array
*/
const listAstronautJobs = (roster) => roster.map(roster => roster.job)

const exampleRoster = [
  {a:1, b:2, job:"Shuttle DJ"},
  {a:1, b:2, job:"Space Cook"}
]

test('test that show function return only a list of objects job attribute', () => {
  expect(
    listAstronautJobs(exampleRoster)
  ).toStrictEqual(
    ["Shuttle DJ", "Space Cook"]
  )
})