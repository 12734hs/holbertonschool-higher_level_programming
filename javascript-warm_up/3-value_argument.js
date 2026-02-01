#!/usr/bin/node

const massivOfArguments = process.argv;

if (massivOfArguments.length === 2) {
  console.log('No argument');
} else {
  console.log(massivOfArguments[2]);
}
