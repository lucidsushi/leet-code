const addJobToAstronaut = (astronaut, job) => {
  astronaut.job = job
  return astronaut
}

const exampleAstronaut = {
  firstName:"Chris",
  lastName: "Hadfield",
  nickname:"Space Oddity",
  prefix:"Astronaut"
}

test('assign job attr to astronaut object', () => {
  expect(
    addJobToAstronaut(exampleAstronaut, "Sushi Chef")
  ).toStrictEqual(
    {
      firstName:"Chris",
      lastName: "Hadfield",
      nickname:"Space Oddity",
      prefix:"Astronaut",
      job:"Sushi Chef"
    }
  )
})