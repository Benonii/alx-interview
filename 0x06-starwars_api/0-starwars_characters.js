#!/usr/bin/node

const request = require('request');
const util = require('util');
const movieId = process.argv[2];
const requestPromise = util.promisify(request);

async function getStarWarsCharacters (movieId) {
  let film = {};
  let character = {};
  let options = {
    url: `https://swapi-api.alx-tools.com/api/films/${movieId}`,
    method: 'GET',
    json: true,
    headers: {
      'Content-Type': 'application/json'
    }
  };

  const response = await requestPromise(options);
  if (response.statusCode === 200) {
    film = await response.body;
  } else {
    console.log('Status code:', response.statusCode);
  }

  for (const endpoint of film.characters) {
    options = {
      url: endpoint,
      method: 'GET',
      json: true,
      headers: {
        'Content-Type': 'application/json'
      }
    };

    const response = await requestPromise(options);
    if (response.statusCode === 200) {
      character = await response.body;
    } else {
      console.log('Status code:', response.statusCode);
    }
    console.log(character.name);
  }
}

/*
  const response = await fetch(, {
    method: 'GET',
  });

  if (!response.ok) {
    throw new Error('response error');
  }

  const film = await response.json();

  for (const endpoint of film.characters) {
    const characterResponse = await fetch(endpoint, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    });

    if (!characterResponse.ok) {
      throw new Error('response error');
    }

    // console.log('Character details: ', characterResponse);
    const character = await characterResponse.json();
    console.log(character.name);
  }
} */

getStarWarsCharacters(movieId);
