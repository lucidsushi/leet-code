
const parseMessage = (origin, message) => `${origin}: ${message}`

test('in = out', () => {
    expect(
        parseMessage("Mission Control", "Hello there!")
    ).toBe(
        "Mission Control: Hello there!"
    )
})
