const chooseLunchWinner = (listOfChoices) => {
  let food_choice = []
  listOfChoices.forEach(function(choice){
    if (food_choice.length == 0) {
      food_choice.push(choice)
    } else if (choice != food_choice[0]) {
      food_choice.pop()
    } else {
      food_choice.push(choice)
    }
  })
  return food_choice.pop()
}

const chooseLunchWinner2 = (listOfChoices) => listOfChoices.sort()[listOfChoices.length>>1]

// always two choices and odd votes
const listOfChoices = [
  "Chicken Dinner",
  "Chicken Dinner",
  "Chicken Dinner",
  "Ice Cream Sandwich", 
  "Ice Cream Sandwich"
]

test('chooseLunchWinner returns value of majority choice', () => {
  expect(chooseLunchWinner(listOfChoices)).toBe("Chicken Dinner")
  expect(chooseLunchWinner2(listOfChoices)).toBe("Chicken Dinner")
})