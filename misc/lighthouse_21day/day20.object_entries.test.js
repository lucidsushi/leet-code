const confirmReentryPlans = (speed, missionData, checks) => {

  const speed_within_limit = (checks.minSpeed <= speed && speed <= checks.maxSpeed)
  if (!speed_within_limit) { return false }
  
  return Object.entries(missionData).every(
  	([type, data]) => data.length === checks.dataEntries[type]
  )
}

/*
The Object.entries() method returns an array of a given object's own enumerable
string-keyed property [key, value] pairs. This is the same as iterating with a
for...in loop, except that a for...in loop enumerates properties in the prototype chain
as well.

const object1 = {
  a: 'somestring',
  b: 42
};
for (const [key, value] of Object.entries(object1)) {
  console.log(`${key}: ${value}`);
}
// expected output:
// "a: somestring"
// "b: 42
*/

const speed = 40
const missionData = {
  astro:["...","..."], 
  bio:["..."], 
  physics:["..."]
}
const checks = {maxSpeed:50, minSpeed:20, dataEntries:{astro:3, bio:1, physics:1}}
const checks2 = {maxSpeed:50, minSpeed:20, dataEntries:{astro:2, bio:1, physics:1}}
const checks3 = {maxSpeed:30, minSpeed:20, dataEntries:{astro:2, bio:1, physics:1}}

test('returns true if speed is within range and dataEntries count is correct', () => {
  expect(confirmReentryPlans(speed, missionData, checks)).toBe(false)
  expect(confirmReentryPlans(speed, missionData, checks2)).toBe(true)
  expect(confirmReentryPlans(speed, missionData, checks3)).toBe(false)
})
