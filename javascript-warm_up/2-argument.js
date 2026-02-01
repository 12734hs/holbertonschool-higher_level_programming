#!/usr/bin/node

const massivOfArguments = process.argv;
console.log(massivOfArguments);

if (massivOfArguments.length == 2) {
  console.log('No argument');
} else if (massivOfArguments.length == 3) {
  console.log('Argument found');
} else {
  console.log('Arguments fount');
}

