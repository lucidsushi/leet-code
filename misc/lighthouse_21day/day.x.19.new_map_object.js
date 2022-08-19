// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map

let john = {name: 'John Doe'},
    lily = {name: 'Lily Bush'},
    peter = {name: 'Peter Drucker'};
const a = new Map([
  [john, 'admin'],
  [lily, 'editor'],
  [peter, 'subscriber']
]);
const aValues = a.values();
console.log(a);
console.log(aValues.next());
console.log(aValues.next());
console.log(aValues.next());


/*
Map {}
    {name: "John Doe"}: "admin"
    {name: "Lily Bush"}: "editor"
    {name: "Peter Drucker"}: "subscriber"

{value: "admin", done: false}
{value: "editor", done: false}
{value: "subscriber", done: false}
*/