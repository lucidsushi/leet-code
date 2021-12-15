
// unpack object as variable
const bookFreePlatform = (platformList, missionDate) => {
  platformList.find(({ bookDate }) => bookDate === undefined).bookDate = missionDate
  return platformList
}
/*
The find() method returns the value of the first element in the provided array that
satisfies the provided testing function. If no values satisfy the testing function,
undefined is returned.
*/
const missionDate = "2021-12-12"
const platformList = [
  {
    name:"Platform A",
    bookDate:"2021-12-11"
  },
  {
    name:"Platform B",
    bookDate:undefined
  },
  {
    name:"Platform C",
    bookDate:undefined
  },
] 

test('missionDate is being to assigned to first object with undefined bookDate', () => {
  expect(
    bookFreePlatform(platformList, missionDate)
  ).toStrictEqual(
    [
      {
        name:"Platform A",
        bookDate:"2021-12-11"
      },
      {
        name:"Platform B",
        bookDate:"2021-12-12"
      },
      {
        name:"Platform C",
        bookDate:undefined
      },
    ]
  )
})