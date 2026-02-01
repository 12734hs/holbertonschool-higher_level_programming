#!/usr/bin/node

const number = Number(process.argv[2]);
if (Number.isNaN(number)) {
  for (let i = 0; i < number + 1; i++) {
    for (let y = 0; y < i; y++) {
      console.log('X');
    }
  }
}
