#!/usr/bin/node
// a script that prints the number of movies
// where the character “Wedge Antilles” is present.
const process = require('process');
const request = require('request');

const url = process.argv[2];
const characterId = '18';
let count = 0;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(characterId)) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
