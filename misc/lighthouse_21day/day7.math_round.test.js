
const storeWeatherConditions = (temperature, condition, windSpeed, windDirection) => {
  weather_conditions = {
    temperature: Math.round((temperature-32)*5/9),
    windSpeed: Math.round(windSpeed/2.234),
    windDirection: windDirection,
    condition: condition
  }
  return weather_conditions
}

const temperature = 32
const condition = "Sunny with small clouds"
const windSpeed = 20
const windDirection = "NNE"

test('purely rounded unit conversion', () => {
  expect(
    storeWeatherConditions(temperature, condition, windSpeed, windDirection)
  ).toStrictEqual(
    {
      temperature:0,
      windSpeed:9,
      windDirection:"NNE",
      condition:"Sunny with small clouds"
    }
  )
})