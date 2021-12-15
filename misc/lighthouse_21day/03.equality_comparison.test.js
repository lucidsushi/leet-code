const checkGaugeStatus = (gauge) => (
    gauge.max > gauge.current && gauge.current > gauge.min ? true : false
)

test.each`
             exampleGauge               | expected
  ${{current: 0.4, min: 0.1, max: 0.5}} | ${true} 
  ${{current: 1.4, min: 0.1, max: 0.4}} | ${false}
  ${{current: 0.1, min: 0.2, max: 0.4}} | ${false}
`('current must be in range in $exampleGauge', ({exampleGauge, expected}) => {
  expect(checkGaugeStatus(exampleGauge)).toBe(expected);
})