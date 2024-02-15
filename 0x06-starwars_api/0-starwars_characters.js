#!/usr/bin/node

const request = require('request');
const utility = require('util');

const MOVIE = process.argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${MOVIE}`;

const get = utility.promisify(request.get);

request.get(URL, async (err, res) => {
  if (err) {
    return;
  }
  const characters = await JSON.parse(res.body).characters;
  await printCharacters(characters);
});

async function printCharacters (characters) {
  const charList = [];

  for (const charUri of characters) {
    await get(charUri).then(res => {
      const character = JSON.parse(res.body);
      charList.push(character.name);
    });
  }

  for (const char of charList) {
    console.log(char);
  }
}