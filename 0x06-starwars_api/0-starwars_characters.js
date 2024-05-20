#!/usr/bin/node

const movieId = process.argv[2];

async function getStarWarsCharacters (movieId) {
  const response = await fetch(`https://swapi-api.alx-tools.com/api/films/${movieId}`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    }
  });

  if (!response.ok) {
    throw new Error('response error');
  }

  const film = await response.json();
  // console.log(film.characters);

  for (const endpoint of film.characters) {
    // console.log(typeof endpoint);
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
}

getStarWarsCharacters(movieId);
