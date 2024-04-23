#!/usr/bin/node

const filesys = require('fs');
filesys.readFile(process.arg[v2], 'utf-8',
  function(err, data) {
    if (err) {
      console.log(err);
      return;
    }
    console.log(data);
  });
