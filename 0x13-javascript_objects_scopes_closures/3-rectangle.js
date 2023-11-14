#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let n = '';
      for (let j = 0; j < this.width; j++) {
        n += 'X';
      }
      console.log(n);
    }
  }
}

module.exports = Rectangle;
