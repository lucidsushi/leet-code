
const getAverageSpeed = (firstPosition, secondPosition) => {
  const {time: time1, altitude: alt1} = firstPosition
  const {time: time2, altitude: alt2} = secondPosition
  //   return parseFloat(
  //     ((alt2-alt1)/(time2-time1)).toFixed(1)
  // )
  return Math.round(
    ((alt2-alt1)/(time2-time1))*10)/10  // *10/10 <-- weird trick to round to 1 decimal
}

const firstPosition = {
  time: 1637074462,
  altitude: 1100
}
const secondPosition = {
  time: 1637074558,
  altitude: 2200
}

test('getAverageSpeed returns average to first decimal point', () => {
  expect(getAverageSpeed(firstPosition, secondPosition)).toBe(11.5)
})