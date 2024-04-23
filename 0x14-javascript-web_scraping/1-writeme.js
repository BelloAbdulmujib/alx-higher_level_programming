#!/usr/bin/node

const filesys = require('fs');
filesys.write(process.arg[v2], write.arg[v3], 'utf-8',
  function(err, data) {
	if (err) {
	  console.log(err);
	  return;
	}
	console.log(data);
  });
