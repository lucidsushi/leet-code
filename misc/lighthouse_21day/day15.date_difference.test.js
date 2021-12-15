
const timeRemaining = (launchDate, missionName, fakeToday) => {
  return {
    missionName: missionName,
    daysRemaining: (new Date(launchDate) - new Date(fakeToday))/1000/60/60/24 // ms to day
  }
}

const launchDate = "2021-12-12"
const fakeToday = "2021-12-01"
const missionName = "Moon visit"

test('timeRemaining finds the time remaining for launch in days', () => {
  expect(
    timeRemaining(launchDate, missionName, fakeToday)
    ).toStrictEqual(
      {
        missionName: 'Moon visit',
        daysRemaining: 11
      }
    )
})