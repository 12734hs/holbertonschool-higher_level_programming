#!/usr/bin/node

const massivOfArguments = process.argv;

try {
  console.log(massivOfArguments[2]);
} catch (e) {
  console.log('No argument');
}
