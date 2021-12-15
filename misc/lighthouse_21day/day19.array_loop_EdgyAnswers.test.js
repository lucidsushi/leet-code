const organizeData = (receivedData) => {

  const summary = {}
  for (const item of receivedData) {
      if (summary[item.type] === undefined) {
          summary[item.type] = [item.data]
      } else {
          summary[item.type].push(item.data)
      }
  }
  return summary
}

const organizeData2 = receivedData => receivedData.reduce((p, c) =>
    ({...p, [c.type]: [p[c.type], c.data].flat().filter(Boolean)}), {})

const organizeData3 = (receivedData) => receivedData.reduce((p, c) =>
    ({...p, [c.type]: [...(p[c.type] || []), c.data]}), {})


const listOfReceivedData = [
  {type: "astro", data: "Saturn Data"},
  {type: "bio", data: "Space Potatoes"},
  {type: "physics", data: "Lagrange Points"},
  {type: "bio", data: "OMG Tardigrades"},
  {type: "physics", data: "Material reflectivity"},
  {type: "astro", data: "Mercury is not the hottest"},
]
const output = {
  astro: ["Saturn Data", "Mercury is not the hottest"],
  bio: ["Space Potatoes", "OMG Tardigrades"],
  physics: ["Lagrange Points", "Material reflectivity"]
}

test('organizeData returns an object of type: [combined_data]', () => {
  expect(organizeData(listOfReceivedData)).toStrictEqual(output)
  expect(organizeData2(listOfReceivedData)).toStrictEqual(output)
  expect(organizeData3(listOfReceivedData)).toStrictEqual(output)
})