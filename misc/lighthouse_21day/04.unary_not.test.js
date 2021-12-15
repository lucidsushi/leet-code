
const switchToggle = (toggle) => {
  toggle.isOn = !toggle.isOn
  return toggle
}
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#unary_operators
test.each`
             toggle           | expected
  ${{name: "A", isOn: false}} | ${{name: "A", isOn: true}}
  ${{name: "A", isOn: true}}  | ${{name: "A", isOn: false}}
`('toggle isOn in $toggle from current value', ({toggle, expected}) => {
  expect(switchToggle(toggle)).toStrictEqual(expected);
})