
const switchSpecificToggle = (toggleList, specificToggle) => {
  toggleList.forEach(
    function(toggle){
      if (toggle.name == specificToggle) {
          toggle.isOn = true   
      }
    }
  )
  return toggleList
}

const toggleList = [
  {name: "toggleA", isOn: false}, 
  {name: "toggleB", isOn: true},
  {name: "toggleC", isOn: false}
]
const specificToggle = "toggleA"
    
test('switchSpecificToggle switches only the specific toggle on', () => {
  expect(switchSpecificToggle(toggleList, specificToggle)).toStrictEqual([
    {
      name: "toggleA",
      isOn: true
    }, 
    {
      name: "toggleB",
      isOn: true
    },
    {
      name: "toggleC",
      isOn: false
    }
  ])
})