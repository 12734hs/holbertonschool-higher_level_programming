#!/usr/bin/node

const massivOfArguments = process.argv;

if (Number(massivOfArguments[2] === 'NaN' || massivOfArguments[2] === undefined) {
  console.log('Not a number');
} else {
  console.log(`My number: ${massivOfArguments[2]}`)
}
