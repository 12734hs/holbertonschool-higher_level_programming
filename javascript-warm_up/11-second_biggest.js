#!/usr/bin/node

const massiv = process.argv.slice(2);
massiv.sort((a, b) => b - a);
console.log(massiv[1]);
