#!/usr/bin/node
if (process.argv[2] === undefined || process.argv[3] === undefined) {
  console.log(0);
} else {
  let m = process.argv[2];
  let n = process.argv[2];
  for (let i = 3; i < process.argv.length; i++) {
    if (process.argv[i] > m) {
      m = process.argv[i];
    }
  }
  for (let i = 2; i < process.argv.length; i++) {
    if (process.argv[i] > n && process.argv[i] != m) {
      n = process.argv[i];
    }
  }
  console.log(Number(n));
}
