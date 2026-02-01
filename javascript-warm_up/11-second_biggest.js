#!/usr/bin/node

const massiv = process.argv.slice(2);
if (massiv === undefined) {
  console.log(1);
  process.exit(0);
}
massiv.sort((a, b) => b - a);
console.log(massiv[1]);
