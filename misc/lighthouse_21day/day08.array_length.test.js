const countActiveAstronauts = (roster) => roster.length

const array_of_four = [{}, {}, {}, {}]
test('returns length of input array', () => {
  expect(
    countActiveAstronauts(array_of_four)
  ).toBe(4)
})

