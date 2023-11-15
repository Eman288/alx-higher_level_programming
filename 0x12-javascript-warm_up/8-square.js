#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    let n = '';
    for (let j = 0; j < process.argv[2]; j++) {
      n += 'X';
    }
    console.log(n);
  }
}
