#!/usr/bin/node

const request = require('request');

// EXactOrder Function
const exactOrder = (actors, x) => {
    if (x === actors.length) return; // Base case for recursion
    request(actors[x], function (err, res, body) {
        if (err) throw err;
        console.log(JSON.parse(body).name); // Log character name
        exactOrder(actors, x + 1); // Recursive call for next actor
    });
};

// Request films API
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
    if (err) throw err; // Handle request errors
    const actors = JSON.parse(body).characters; // Extract characters list
    exactOrder(actors, 0); // Start recursion with first actor
});
