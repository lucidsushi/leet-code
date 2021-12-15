const switchAllTogglesOn = toggleList =>
  toggleList.forEach(toggle => toggle.isOn = true)
  || toggleList
// toggleList => toggleList.map(toggle => (toggle.isOn = true) && toggle)

// The forEach() method executes a provided function once for each array element.

test('switchAllTogglesOn turns all toggles on', () => {
  expect(
    switchAllTogglesOn(
      [
        {
          name:"Air",
          isOn:true
        },
        {
          name:"Radio",
          isOn:false
        },
      ]
    )
  ).toStrictEqual(
    [
      {
        name:"Air",
        isOn:true
      },
      {
        name:"Radio",
        isOn:true
      },
    ]
  )
})
