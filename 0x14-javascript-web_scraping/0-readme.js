#!/usr/bin/node

const filesys = require('filesys');
filesys.readFile(process.arg[v2], 'utf-8',
  function(error, data) {
    if (error) {
      console.log(error);
      return;
    }
    console.log(data);
  });
