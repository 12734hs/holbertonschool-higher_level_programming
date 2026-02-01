#!/usr/bin/node

const number = Number(process.argv[2]);

function factorial(num) {
  if (Number.isNaN(num) || num < 0) return 'Not a number';

  let result = 1;
  for (let i = 1; i <= num; i++) {
    result *= i; 
  }

  return result;
}
