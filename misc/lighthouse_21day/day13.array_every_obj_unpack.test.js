const checkAllGauges = (gaugeList) => gaugeList.every(
  ({min, current, max}) => (min < current && current < max)
)
/*
The every() method tests whether all elements in the array pass the test implemented by
the provided function. It returns a Boolean value.
*/

const gaugeList = [
  {
    current:0.4,
    min:0.1,
    max:0.9
  },
  {
    current:1.2, // out of range
    min:0.1,
    max:0.6
  }
]
const gaugeList_good = [
  {
    current:0.4,
    min:0.1,
    max:0.9
  },
  {
    current:0.2,
    min:0.1,
    max:0.6
  }
]

test('return false if any gauge is out of range', () => {
  expect(checkAllGauges(gaugeList)).toBe(false)
})
test('return true if all gauges are in range', () => {
  expect(checkAllGauges(gaugeList_good)).toBe(true)
})