const parseTranscripts = messages => 
messages.map(({ origin, message }) => `${origin}: ${message}`)

const messages = [
  {origin:"MC", message:"Hello!"},
  {origin:"Shuttle", message:"Hey!"},
]

test('takes array of objects and returns concatenated string', () => {
  expect(
    parseTranscripts(messages)
  ).toStrictEqual(
    ["MC: Hello!", "Shuttle: Hey!"]
  )
})