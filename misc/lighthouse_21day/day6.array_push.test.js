
const addAstronautToRoster = (roster, astronaut) => {
  roster.push(astronaut)
  return roster  
}

const exampleRoster = []
const exampleAstronaut = {
  firstName:"Chris",
  lastName: "Hadfield",
  nickname:"Space Oddity",
  prefix:"Astronaut"
}

test('push object into array', () => {
  expect(
    addAstronautToRoster(exampleRoster, exampleAstronaut)
  ).toStrictEqual(
    [
      {
        firstName:"Chris",
        lastName: "Hadfield",
        nickname:"Space Oddity",
        prefix:"Astronaut"
      }
    ]
  )
})