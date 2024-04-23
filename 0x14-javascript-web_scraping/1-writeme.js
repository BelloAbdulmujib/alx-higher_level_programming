#!/usr/bin/node

const fs = require('fs');
fs.writeFile(process.arg[v2], process.arg[v3], 'utf-8',
  function(err) {
	if (err) {
	console.log(err);
	}
  });
