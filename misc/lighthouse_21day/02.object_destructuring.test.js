const generateAstronautTag = (astronaut) => {
    const {firstName, nickname, prefix} = astronaut
    return `${prefix}: ${firstName} "${nickname}" ${astronaut.lastName}`
}

const exampleAstronaut = {
    firstName: "Yuri",
    lastName: "Gagarin",
    nickname: "First!",
    prefix: "Cosmonaut"
}

test('in = out', () => {
    expect(
        generateAstronautTag(exampleAstronaut)
    ).toBe(
        'Cosmonaut: Yuri "First!" Gagarin'
    )
})
